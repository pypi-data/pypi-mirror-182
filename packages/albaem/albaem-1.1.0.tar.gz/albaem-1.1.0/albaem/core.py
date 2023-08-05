import time
import socket
import logging.handlers
from threading import Lock

RANGES = ['1mA', '100uA', '10uA', '1uA', '100nA', '10nA', '1nA', '100pA']


class AlbaEm:
    """
    This is the main library used for the communications with Alba
    electrometers.
    The configuration of the serial line is:
        8bits + 1 stop bit, bdr: 9600, terminator:none
    The cable is crossed
    """
    def __init__(self, host, port=7):

        self.logger = logging.Logger("albaEmLIB")
        self.logger.setLevel(logging.INFO)

        self.host = host
        self.port = port
        self.lock = Lock()
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # @deprecated: it seems not useful nevermore.
        self.sock.settimeout(0.3)
        self.offset_corr_alarm = False
        self.saturation_list = ''
        self.stateMoving = False

    def ask(self, cmd, size=8192):
        """
        Basic method for send commands to the Alba Electrometer.
        @param cmd: Command for send to electrometer.
        @param size: Default value is 8192. This param is the maximum
                     amount of data to be received at once.
        @return: Data received from Alba electrometer.
        """

        try:
            # @todo: wait until \x00 has arrived as answer.

            self.lock.acquire()
            self.sock.sendto(cmd.encode(), (self.host, self.port))
            data = ''
            while not data.endswith('\x00'):
                answer = self.sock.recv(size).decode()
                data = data + answer
            self.Command = cmd + ': ' + str(data) + '\n'

            if data.startswith('?ERROR') or data.startswith('ERROR'):
                self.logger.debug('Command: %s Data: %s', cmd, data)

            elif not data.startswith(cmd.split()[0]):
                self.logger.debug('Command: %s Data: %s', cmd, data)
                # @todo: should be raise an exception?
                raise socket.timeout
            else:
                self.logger.debug('AlbaEM DEBUG: query: %s\t'
                                  'answer length: %d\tanswer:#%s#', cmd,
                                  len(data), data)
                return data

        except socket.timeout:
            self.logger.error(
                'Timeout Error in method ask sending the command: %s', cmd)
            try:
                timesToCheck = 50
                data = ''
                while timesToCheck > 0:
                    timesToCheck -= 1
                    while not data.endswith('\x00'):
                        answer = self.sock.recv(size).decode()
                        data = data + answer
                    self.Command = cmd + ': ' + str(data) + '\n'
                    if data.startswith('?ERROR') or data.startswith('ERROR'):
                        self.logger.error(
                            'Error reading the command %s again after a '
                            'timeout', self.Command)
                        raise Exception(
                            f'Error reading the command {self.Command} again '
                            f'after a timeout')
                    elif not data.startswith(cmd.split()[0]):
                        self.logger.debug('Command: %s Data: %s', cmd, data)
                        raise Exception(
                            f'Error reading the command {self.Command} again '
                            f'after a timeout')
                    else:
                        return data
            except Exception as e:
                self.logger.error('Unknown error in method ask. %s', e)
                raise

        except socket.error as error:
            self.logger.error('Socket Error in method ask/sending the '
                              'command: %s. Error: %s', self.Command, error)
            raise
        except Exception as e:
            self.logger.error('Unknown error in method ask/sending the '
                              'command: %s. Error: %s', self.Command, e)
            raise

        finally:
            self.lock.release()

    def extractMultichannel(self, chain, initialpos):
        """
        This method cleans the answer from alba electrometer and returns only
        the important data.
        @param chain: String to extract the useful data.
        @param initialpos: initial position of the string with useful data.

        @return: Useful data obtained from the albaem answer.
        """
        answersplit = chain.strip('\x00').split(' ')

        if answersplit[0] in ['?MEAS', '?IINST', '?LDATA', '?DATA']:
            status = answersplit[len(answersplit) - 1]
            parameters = answersplit[initialpos:len(answersplit) - 1]
        else:
            status = ''
            parameters = answersplit[initialpos:len(answersplit)]

        if answersplit[0] == '?AVDATA':
            return list(map(float, parameters))

        couples = []
        if len(parameters) % 2 != 0:
            self.logger.error(
                'Error @extractMultichannel. Parameters: %s Command: %s',
                str(parameters),
                self.Command)
            raise Exception('extractMultichannel: Wrong number of parameters')
        for i in range(0, len(parameters) // 2):
            if parameters[i * 2] in ['1', '2', '3', '4']:
                couples.append([parameters[i * 2], parameters[i * 2 + 1]])
            else:
                self.logger.error(
                    'Error @extractMultichannel. Parameters: %s Command: %s',
                    str(parameters),
                    self.Command)
                raise Exception('extractMultichannel: Wrong channel')
        self.logger.debug("extractMultichannel:%s", couples)
        if answersplit[0] == '?MEAS' or answersplit[0] == '?IINST':
            return couples, status
        elif answersplit[0] == '?LDATA' or answersplit[0].startswith('?DATA'):
            lastpos = answersplit[1]
            return couples, status, lastpos
        else:
            return couples

    def extractSimple(self, chain):
        """
        Do the same as extractMultichannel, but it is used when the answer
        from electrometer is only one word.
        @param chain: String to extract the useful data.

        @return: Useful data obtained from the albaem answer.
        """
        data = chain.strip('\x00').split(' ')[1]
        return data

    def _getChannelsFromList(self, channels):
        """
        Method to receive the channels as a list of integers
        and transform it to a string to add to the command to send.
        @param channels: List of channels to add to the command.

        @return: string with the channels
        """
        channelChain = ''
        for channel in channels:
            channelChain = '%s %s ' % (channelChain, channel)
        return channelChain

    def _prepareChannelsAndValues(self, valuesAndChannelsList):
        """
        Method to receive the channels as a list of integers
        and transform it to a string to add to the command to send.
        @param valuesAndChannelsList: List of channels to add to the command.

        @return: string with the channels
        """
        channelChain = ''
        for couple in valuesAndChannelsList:
            channelChain = '%s %s %s' % (channelChain, couple[0], couple[1])

        return channelChain

    def getAutoRangeMin(self, channels):
        """
        Method to get the autoRangeMin for each channel.
        @param channels: List of channels to obtain the data.

        @return: list of channels and autoranges
        """

        channelChain = self._getChannelsFromList(channels)
        answer = None
        try:
            command = '?AUTORANGEMIN %s' % channelChain
            answer = self.ask(command)
            self.logger.debug(
                "getAutoRangeMin: SEND: %s\t RCVD: %s" %
                (command, answer))
            autoRangeMin = self.extractMultichannel(answer, 1)

        except Exception as e:
            self.logger.error('getAutoRangeMin: %s', e)
            raise
        self.logger.debug(
            "getAutoRangeMin: SEND: %s\t RCVD: %s", command, answer)
        self.logger.debug("getAutoRangeMin: %s", autoRangeMin)
        return autoRangeMin

    def getAllAutoRangesMin(self):
        """
        Method for getting the autorangeMin of each channel.

        @return: State of autorangeMin
        """
        return self.getAutoRangeMin(['1', '2', '3', '4'])

    def _setAutoRangeMin(self, autoRangesMin):
        """
        """
        channelChain = self._prepareChannelsAndValues(autoRangesMin)
        answer = None
        try:
            command = f'AUTORANGEMIN {channelChain}'
            answer = self.ask(command)

            if answer != 'AUTORANGEMIN ACK\x00':
                raise Exception('setAutoRangesMin: Wrong acknowledge')
        except Exception as e:
            raise Exception(f'setAutoRangesMin: {e}')
        self.logger.debug('setAutoRangesMin: SEND: %s\t RCVD: %s', command,
                          answer)

    def setAutoRangeMin(self, autoRangeMin):
        """
        Method to set the autoRangeMin for each channel in the list.
        @param autoRangeMin: List of channels and values
        """
        state = self.getState()
        if state == 'RUNNING':
            self.Stop()
        self.StopAdc()
        self._setAutoRangeMin(autoRangeMin)
        self.StartAdc()

    def setAllAutoRangesMin(self, autoRangeMin):
        """
        Method to set the autoRangeMin for all channels.
        @param autoRangeMin in %
        """
        state = self.getState()
        if state == 'RUNNING':
            self.Stop()
        self.StopAdc()
        self._setAutoRangeMin([['1', autoRangeMin], ['2', autoRangeMin], [
                              '3', autoRangeMin], ['4', autoRangeMin]])
        self.StartAdc()

    def getAutoRangeMax(self, channels):
        """
        Method to get the autoRangeMax for each channel.
        @param channels: List of channels to obtain the data.

        @return: list of channels and autoranges
        """
        channelChain = self._getChannelsFromList(channels)

        try:
            command = '?AUTORANGEMAX %s' % channelChain
            answer = self.ask(command)
            self.logger.debug("getAutoRangeMax: SEND: %s\t RCVD: %s",
                              command, answer)
            autoRangeMax = self.extractMultichannel(answer, 1)

        except Exception as e:
            self.logger.error('getAutoRangeMax: %s' % e)
            raise
        self.logger.debug("getAutoRangeMax: SEND: %s\t RCVD: %s", command,
                          answer)
        self.logger.debug("getAutoRangeMax: %s", autoRangeMax)
        return autoRangeMax

    def getAllAutoRangesMax(self):
        """
        Method for getting the autorangeMax of each channel.
        @return: State of autorangeMax
        """
        return self.getAutoRangeMax(['1', '2', '3', '4'])

    def _setAutoRangeMax(self, autoRangesMax):
        """
        """
        channelChain = self._prepareChannelsAndValues(autoRangesMax)
        try:
            command = f'AUTORANGEMAX {channelChain}'
            answer = self.ask(command)

            if answer != 'AUTORANGEMAX ACK\x00':
                raise Exception('setAllAutoRangesMax: Wrong acknowledge')
        except Exception as e:
            raise Exception('setAllAutoRangesMax: %s' % e)
        self.logger.debug('setAllAutoRangesMax: SEND: %s\t RCVD: %s',
                          command, answer)

    def setAutoRangeMax(self, autoRangeMax):
        """
        Method to set the autoRangeMax for each channel in the list.
        @param autoRangeMax: List of channels and values
        """
        state = self.getState()
        if state == 'RUNNING':
            self.Stop()
        self.StopAdc()
        self._setAutoRangeMax(autoRangeMax)
        self.StartAdc()

    def setAllAutoRangesMax(self, autoRangeMax):
        """
        Method to set the autoRangeMax for all channels.
        @param autoRangeMax in %
        """
        state = self.getState()
        if state == 'RUNNING':
            self.Stop()
        self.StopAdc()
        self._setAutoRangeMax([['1', autoRangeMax], ['2', autoRangeMax],
                               ['3', autoRangeMax], ['4', autoRangeMax]])
        self.StartAdc()

    def getAutoRange(self, channels):
        """
        Method to get the autoRange for each channel.
        @param channels: List of channels to obtain the data.

        @return: list of channels and autoranges
        """

        channelChain = self._getChannelsFromList(channels)
        try:
            command = f'?AUTORANGE {channelChain}'
            answer = self.ask(command)
            self.logger.debug("getAutoRange: SEND: %s\t RCVD: %s", command,
                              answer)
            autoRange = self.extractMultichannel(answer, 1)

        except Exception as e:
            self.logger.error('getAutoRanges: %s', e)
            raise
        self.logger.debug("getAutoRanges: SEND: %s\t RCVD: %s", command,
                          answer)
        self.logger.debug("getAutoRanges: %s", autoRange)
        return autoRange

    def getAllAutoRanges(self):
        """
        Method for getting the autorange of each channel.
        @return: State of autorange
        """
        return self.getAutoRange(['1', '2', '3', '4'])

    def _setAutoRange(self, autoRanges):
        """
        """
        channelChain = self._prepareChannelsAndValues(autoRanges)
        try:
            command = f'AUTORANGE {channelChain}'
            answer = self.ask(command)

            if answer != 'AUTORANGE ACK\x00':
                raise Exception('setAllAutoRanges: Wrong acknowledge')
        except Exception as e:
            raise Exception(f'setAllAutoRanges: {e}')
        self.logger.debug('setAllAutoRanges: SEND: %s\t RCVD: %s', command,
                          answer)

    def setAutoRange(self, autoRange):
        """
        Method to set the autoRange for each channel in the list.
        @param autoRange: List of channels and values
        """
        state = self.getState()
        if state == 'RUNNING':
            self.Stop()
        self.StopAdc()
        self._setAutoRange(autoRange)
        self.StartAdc()

    def setAllAutoRanges(self, autoRange):
        """
        Method to set the autoRange for all channels.
        @param autoRange: {YES | NO}
        """
        state = self.getState()
        if state == 'RUNNING':
            self.Stop()
        self.StopAdc()
        self._setAutoRange([['1', autoRange], ['2', autoRange],
                            ['3', autoRange], ['4', autoRange]])
        self.StartAdc()

    def getRanges(self, channels):
        """
        Method for read the range in a channel.
        @param channels: List of channels to obtain the range.

        @return: List of ranges.
        """

        channelChain = self._getChannelsFromList(channels)
        try:
            command = f'?RANGE {channelChain}'
            answer = self.ask(command)
            self.logger.debug("getRanges: SEND: %s\t RCVD: %s", command,
                              answer)
            ranges = self.extractMultichannel(answer, 1)
        except Exception as e:
            self.logger.error("getRanges: %s", e)
            raise
        self.logger.debug("getRanges: SEND: %s\t RCVD: %s", command,
                          answer)
        self.logger.debug("getRanges: %s", ranges)
        return ranges

    def getRangesAll(self):
        """
        Method for read all the ranges.
        @return: List of ranges.
        """
        return self.getAutoRange(['1', '2', '3', '4'])

    def _setRanges(self, ranges):
        """
        Method for set Ranges.
        @param ranges: list of ranges to set.
        """
        channelChain = self._prepareChannelsAndValues(ranges)
        try:
            command = f'RANGE {channelChain}'
            answer = self.ask(command)
            if answer != 'RANGE ACK\x00':
                raise Exception('setRanges: Wrong acknowledge')
        except Exception as e:
            raise Exception("setRanges: %s", e)
        self.logger.debug("setRanges: SEND: %s\t RCVD: %s", command, answer)

    def setRanges(self, ranges):
        """
        Method used for setting the ranges of each channel.
        @param ranges: List of channels and values to set.
        """
        state = self.getState()
        if state == 'RUNNING':
            self.Stop()
        self.StopAdc()
        self._setRanges(ranges)
        self.StartAdc()

    def setRangesAll(self, range):
        """
        This Method set all the channels with the same values.
        @param range: Range to apply in all the channels.
        """
        state = self.getState()
        if state == 'RUNNING':
            self.Stop()
        self.StopAdc()
        self.setRanges([['1', range], ['2', range],
                        ['3', range], ['4', range]])
        self.StartAdc()

    def getEnables(self, channels):
        """
        Method to get the enables of each channel.
        @param channels: List of channels to get the enables.
        @return: list of enables.
        """

        channelChain = self._getChannelsFromList(channels)
        try:
            command = f'?ENABLE {channelChain}'
            answer = self.ask(command)
            enables = self.extractMultichannel(answer, 1)
        except Exception as e:
            self.logger.error("getEnables: %s", e)
            raise
        self.logger.debug("getEnables: SEND: %s\t RCVD: %s", command, answer)
        self.logger.debug("getEnables: %s", enables)
        return enables

    def getEnablesAll(self):
        """
        Method to get the enables of all channels.
        @return: list of enables.
        """
        return self.getEnables(['1', '2', '3', '4'])

    def _setEnables(self, enables):

        channelChain = self._prepareChannelsAndValues(enables)
        command = f'ENABLE {channelChain}'
        answer = None
        try:
            answer = self.ask(command)
            if answer != 'ENABLE ACK\x00':
                raise Exception('setEnables: Wrong acknowledge')
        except Exception as e:
            self.logger.error("setEnables: %s", e)
        self.logger.debug("setEnables: SEND: %s\t RCVD: %s", command, answer)

    def setEnables(self, enables):
        state = self.getState()
        if state == 'RUNNING':
            self.Stop()
        self.StopAdc()
        self._setEnables(enables)
        self.StartAdc()

    def setEnablesAll(self, enable):
        state = self.getState()
        if state == 'RUNNING':
            self.Stop()
        self.StopAdc()
        self.setEnables([['1', enable], ['2', enable],
                         ['3', enable], ['4', enable]])
        self.StartAdc()

    def disableAll(self):
        self.setEnables([['1', 'NO'], ['2', 'NO'], ['3', 'NO'], ['4', 'NO']])

    def enableChannel(self, channel):
        self.setEnables([['%s' % channel, 'YES']])

    def getInvs(self, channels):

        channelChain = self._getChannelsFromList(channels)
        try:
            command = f'?INV {channelChain}'
            answer = self.ask(command)
            invs = self.extractMultichannel(answer, 1)
        except Exception as e:
            self.logger.error("getInvs: %s", e)
            raise
        self.logger.debug("getInvs: SEND: %s\t RCVD: %s", command, answer)
        self.logger.debug("getInvs: %s", invs)
        return invs

    def getDInvs(self, channels):
        dinvs = []
        try:
            for channel in channels:
                command = f'?GAINCORR 1mA {channel}'
                answer = self.ask(command)
                self.logger.debug(answer)
                val = float((answer.split(' ')[3].strip('\00')))
                self.logger.debug(answer, val)
                if val < 0:
                    res = 'YES'
                else:
                    res = 'NO'
                dinvs.append([channel, res])
                self.logger.debug("getDInvs: SEND: %s\t RCVD: %s", command,
                                  answer)
        except Exception as e:
            self.logger.error("getDInvs: %s", e)
            raise

        self.logger.debug("getDInvs: %s", dinvs)
        return dinvs

    def getDInvsAll(self):
        return self.getDInvs(['1', '2', '3', '4'])

    def getInvsAll(self):
        return self.getInvs(['1', '2', '3', '4'])

    def _setInvs(self, invs):

        channelChain = self._prepareChannelsAndValues(invs)
        command = f'INV {channelChain}'
        answer = None
        try:
            answer = self.ask(command)
            if answer != 'INV ACK\x00':
                raise Exception('setInvs: Wrong acknowledge')
        except Exception as e:
            self.logger.error("setInvs: %s", e)
        self.logger.debug("setInvs: SEND: %s\t RCVD: %s", command, answer)

    def _setDInvs(self, dinvs):
        for couple in dinvs:
            if couple[1] == 'YES':
                self.toggleGainCorrPolarisation(
                    int(couple[0]), factor=-1, relative=0)
            else:
                self.toggleGainCorrPolarisation(
                    int(couple[0]), factor=1, relative=0)

    def setDInvs(self, dinvs):
        """
        Method to set the digital inversion
        @param dinvs: [['1','YES'|'NO'],...,['4','YES'|'NO']]
        """
        state = self.getState()
        if state == 'RUNNING':
            self.Stop()
        self.StopAdc()
        self._setDInvs(dinvs)

    def setDInvsAll(self, dinv):
        state = self.getState()
        if state == 'RUNNING':
            self.Stop()
        self.StopAdc()
        self.setDInvs([['1', dinv], ['2', dinv], ['3', dinv], ['4', dinv]])
        self.StartAdc()

    def setInvs(self, invs):
        state = self.getState()
        if state == 'RUNNING':
            self.Stop()
        self.StopAdc()
        self._setInvs(invs)
        self.StartAdc()

    def setInvsAll(self, inv):
        state = self.getState()
        if state == 'RUNNING':
            self.Stop()
        self.StopAdc()
        self.setInvs([['1', inv], ['2', inv], ['3', inv], ['4', inv]])
        self.StartAdc()

    def getFilters(self, channels):
        channelChain = self._getChannelsFromList(channels)
        try:
            command = f'?FILTER {channelChain}'
            answer = self.ask(command)
            filters = self.extractMultichannel(answer, 1)
        except Exception as e:
            self.logger.error("getFilters: %s", e)
            raise
        self.logger.debug("getFilters: SEND: %s\t RCVD: %s", command, answer)
        self.logger.debug("getFilters: %s", filters)
        return filters

    def getFiltersAll(self):
        return self.getFilters(['1', '2', '3', '4'])

    def _setFilters(self, filters):
        channelChain = self._prepareChannelsAndValues(filters)
        command = f'FILTER {channelChain}'
        answer = None
        try:
            print("COMMAND: ", command)
            answer = self.ask(command)
            if answer != 'FILTER ACK\x00':
                raise Exception('setFilters: Wrong acknowledge')
        except Exception as e:
            self.logger.error("setFilters: %s", e)
        self.logger.debug("setFilters: SEND: %s\t RCVD: %s", command, answer)

    def setFilters(self, filters):
        state = self.getState()
        if state == 'RUNNING':
            self.Stop()
        self.StopAdc()
        self._setFilters(filters)
        self.StartAdc()

    def setFiltersAll(self, filter_value):
        state = self.getState()
        if state == 'RUNNING':
            self.Stop()
        self.StopAdc()
        self.setFilters([['1', filter_value], ['2', filter_value],
                         ['3', filter_value], ['4', filter_value]])
        self.StartAdc()

    def getOffsets(self, channels):

        channelChain = self._getChannelsFromList(channels)
        try:
            command = f'?OFFSET {channelChain}'
            answer = self.ask(command)
            offsets = self.extractMultichannel(answer, 1)
        except Exception as e:
            self.logger.error("getOffsets: %s", e)
            raise
        self.logger.debug("getOffsets: SEND: %s\t RCVD: %s", command, answer)
        self.logger.debug("getOffsets: %s", offsets)
        return offsets

    def getOffsetsAll(self):
        return self.getOffsets(['1', '2', '3', '4'])

    def _setOffsets(self, offsets):

        channelChain = self._prepareChannelsAndValues(offsets)
        command = f'OFFSET {channelChain}'
        answer = None
        try:
            answer = self.ask(command)
            if answer != 'OFFSET ACK\x00':
                raise Exception('setOffsets: Wrong acknowledge')
        except Exception as e:
            self.logger.error("setOffsets: %s", e)
        self.logger.debug("setOffsets: SEND: %s\t RCVD: %s", command, answer)

    def setOffsets(self, offsets):
        state = self.getState()
        if state == 'RUNNING':
            self.Stop()
        self.StopAdc()
        self._setOffsets(offsets)
        self.StartAdc()

    def setOffsetsAll(self, offset):
        state = self.getState()
        if state == 'RUNNING':
            self.Stop()
        self.StopAdc()
        self.setOffsets([['1', offset], ['2', offset], ['3', offset],
                         ['4', offset]])
        self.StartAdc()

    def getAmpmodes(self, channels):

        channelChain = self._getChannelsFromList(channels)
        try:
            command = f'?AMPMODE {channelChain}'
            answer = self.ask(command)
            ampmodes = self.extractMultichannel(answer, 1)
        except Exception as e:
            self.logger.error("getAmpmodes: %s", e)
            raise
        self.logger.debug("getAmpmodes: SEND: %s\t RCVD: %s", command, answer)
        self.logger.debug("getAmpmodes: %s", ampmodes)
        return ampmodes

    def getAmpmodesAll(self):
        return self.getAmpmodes(['1', '2', '3', '4'])

    def _setAmpmodes(self, ampModes):
        channelChain = ''
        for couple in ampModes:
            channelChain = f'{channelChain} {couple[0]} {couple[1]} '

        channelChain = self._prepareChannelsAndValues(ampModes)
        try:
            command = f'AMPMODE {channelChain}'
            answer = self.ask(command)
            if answer != 'AMPMODE ACK\x00':
                raise Exception('setAmpmodes: Wrong acknowledge')
            self.logger.debug("setAmpmodes: SEND: %s\t RCVD: %s", command,
                              answer)
        except Exception as e:
            self.logger.error("setAmpmodes: %s", e)

    def setAmpmodes(self, ampmodes):
        state = self.getState()
        if state == 'RUNNING':
            self.Stop()
        self.StopAdc()
        self._setAmpmodes(ampmodes)
        self.StartAdc()

    def setAmpmodesAll(self, ampmode):
        state = self.getState()
        if state == 'RUNNING':
            self.Stop()
        self.setAmpmodes([['1', ampmode], ['2', ampmode], ['3', ampmode],
                          ['4', ampmode]])

    def getLdata(self):
        try:
            command = '?LDATA'
            answer = self.ask(command)
            self.logger.info(answer)
            if not answer.startswith('?BUFFER ERROR'):
                measures, status, lastpos = self.extractMultichannel(answer, 2)
                # We use 0 for the case when no data is available
                lastpos = int(lastpos) + 1
            else:
                self.logger.debug('BUFFER ERROR!')
                raise Exception('BUFFER ERROR in getLData!')
        except Exception as e:
            self.logger.error("getLdata: %s", e)
            raise
        self.logger.debug("getLdata: SEND: %s\t RCVD: %s", command, answer)
        self.logger.debug("getLdata: %s, %s %s", measures, status, lastpos)
        return measures, status, lastpos

    def getData(self, position):
        try:
            command = f'?DATA {position}'
            answer = self.ask(command)
            if not answer.startswith('?BUFFER ERROR'):
                measures, status, lastpos = self.extractMultichannel(answer, 2)
                # We use 0 for the case when no data is available
                lastpos = int(lastpos) + 1
            else:
                self.logger.debug('BUFFER ERROR!')
                raise Exception('BUFFER ERROR in getLData!')
        except Exception as e:
            self.logger.error("getData: %s", e)
            raise
        self.logger.debug("getData: SEND: %s\t RCVD: %s", command, answer)
        self.logger.debug("getData: %s, %s, %s", measures, status, lastpos)
        return measures, status, lastpos

    def getLastpos(self):
        measures, status, lastpos = self.getLdata()
        return lastpos

    def getAvData(self, channel):
        buffer = []
        try:
            command = f'?AVDATA {channel}'
            answer = self.ask(command)
            if not answer.startswith('?BUFFER ERROR'):
                buffer = self.extractMultichannel(answer, 1)
        except Exception as e:
            self.logger.error("getAvData: %s", e)
            raise
        self.logger.debug('getAvData: SEND:%s\t RCVD: %s', command, answer)
        self.logger.debug('getAvData: %s', buffer)
        return buffer

    # Deprecated -------------------------------
    def getBuffer(self):
        lastpos = self.getLastpos()
        thebuffer = []
        for i in range(0, lastpos):
            # getLdata() bug included by Mr. JLidon
            measures, status, lastpos = self.getData(i)
            thebuffer.append([float(measures[0][1]), float(
                measures[1][1]), float(measures[2][1]), float(measures[3][1])])
        return thebuffer

    def getBufferChannel(self, chan):
        if chan in range(1, 5):
            abuffer = self.getBuffer()
            channelbuffer = []
            for i in range(0, len(abuffer)):
                channelbuffer.append(abuffer[i][chan - 1])
            return channelbuffer
        else:
            raise Exception('getBufferChannel: Wrong channel (1-4)')
    # -------------------------------

    def _digitalOffsetCorrect(
            self, chans, rang, digitaloffsettarget, correct=1):
        cmd = []
        for ch in chans:
            cmd.append(['%s' % ch, rang])
        print(cmd)
        self.setRanges(cmd)
        time.sleep(0.2)
        measures = self.ask('?VMEAS').strip('\x00').split(' ')

        measures2 = [
            float(
                measures[2]), float(
                measures[4]), float(
                measures[6]), float(
                    measures[8])]
        measures3 = []
        for i in range(0, len(measures2)):
            measures3.append(-measures2[i] + digitaloffsettarget)
        cmdpar = ''
        for i in chans:
            cmdpar = cmdpar + f' {i} {measures3[i - 1]}'
        if correct == 1:
            self.sendSetCmd(f'OFFSETCORR {rang}{cmdpar}')

    def digitalOffsetCorrect(self, chans, ranges='all',
                             digitaloffsettarget=0, correct=1):
        self.stateMoving = True
        oldAvsamples = self.getAvsamples()
        self.setAvsamples(1000)

        if ranges == 'all':
            ranges = RANGES

        digitaloffsettarget = 10.0 * digitaloffsettarget
        for rang in ranges:
            self._digitalOffsetCorrect(
                chans, rang, digitaloffsettarget, correct)
        self.setAvsamples(oldAvsamples)
        self.offset_corr_alarm = False
        self.stateMoving = False
        offsetcorr_all = self.getOffsetCorrAll()
        self.saturation_list = []
        for ran in ranges:
            line = offsetcorr_all.get(ran)
            for l1 in line:
                ch = float(l1[1])
                if -10. <= ch >= 10.:
                    self.offset_corr_alarm = True
                    msg = f"Channel {l1[0]}, Range: {ran} is saturated with " \
                          f"value: {l1[1]}"
                    self.saturation_list.append(msg)

    def digitalOffsetCheck(self):
        self.digitalOffsetCorrect([1, 2, 3, 4], correct=0)

    def configDiagnose(self, chan):
        self.logger.debug('ConfigDiagnose initiating configuration ...')
        self.getInfo()
        self.setAvsamples(1)
        self.setTrigperiod(1)
        self.setPoints(1000)
        self.setTrigmode('INT')
        self.logger.debug('Acquiring ...')
        self.Start()
        time.sleep(2)
        mydata = self.getBufferChannel(chan)
        return mydata

    def getInstantMeasures(self, channels):

        channelChain = self._getChannelsFromList(channels)
        try:
            command = f'?IINST {channelChain}'
            answer = self.ask(command)
            measures, status = self.extractMultichannel(answer, 1)
        except Exception as e:
            self.logger.error("getInstantMeasures: %s", e)
            raise
        self.logger.debug("getInstantMeasures: SEND: %s\t RCVD: %s",
                          command, answer)
        self.logger.debug("getInstantMeasures: %s, %s", measures, status)
        return measures, status

    def getInstantMeasure(self, channel):
        try:
            command = '?IINST'
            answer = self.ask(command)
            measure, status = self.extractMultichannel(answer, 1)
        except Exception as e:
            self.logger.error("getInstantMeasure: %s", e)
            raise
        self.logger.debug("getInstantMeasure: SEND: %s\t RCVD: %s",
                          command, answer)
        self.logger.debug("getInstantMeasure: %s",
                          measure[int(channel[0]) - 1][1])
        return measure[int(channel[0]) - 1][1]
        # return measure, status

    def getInstantMeasuresAll(self):
        return self.getInstantMeasures(['1', '2', '3', '4'])

    def getMeasures(self, channels):

        channelChain = self._getChannelsFromList(channels)
        try:
            command = f'?MEAS {channelChain}'
            answer = self.ask(command)
            measures, status = self.extractMultichannel(answer, 1)
        except Exception as e:
            self.logger.error("getMeasures: %s", e)
            raise
        self.logger.debug("getMeasures: SEND: %s\t RCVD: %s", command, answer)
        self.logger.debug("getMeasures: %s, %s" % (measures, status))
        return measures, status

    def getMeasure(self, channel):
        try:
            command = '?MEAS'
            answer = self.ask(command)
            measure, status = self.extractMultichannel(answer, 1)
        except Exception as e:
            self.logger.error("getMeasure: %s", e)
            raise
        self.logger.debug("getMeasure: SEND: %s\t RCVD: %s", command, answer)
        self.logger.debug("getMeasure: %s, %s" % (measure, status))
        self.logger.debug("getMeasure: %s" % (measure[int(channel[0]) - 1][1]))
        return measure[int(channel[0]) - 1][1]

    def getMeasuresAll(self):
        return self.getMeasures(['1', '2', '3', '4'])

    def getAvsamples(self):
        try:
            command = '?AVSAMPLES'
            answer = self.ask(command)
            avsamples = self.extractSimple(answer)
        except Exception as e:
            self.logger.error("getAvsamples: %s", e)
            raise
        self.logger.debug("getAvsamples: SEND: %s\t RCVD: %s", command, answer)
        self.logger.debug("getAvsamples: %s", avsamples)
        return avsamples

    def _setAvsamples(self, avsamples):
        command = f'AVSAMPLES {avsamples}'
        answer = None
        try:
            command = f'AVSAMPLES {avsamples}'
            answer = self.ask(command)
            if answer != 'AVSAMPLES ACK\x00':
                raise Exception('setAvsamples: Wrong acknowledge')
        except Exception as e:
            self.logger.error("setAvsamples: %s", e)
            self.logger.error("setAvsamples: SEND: %s\t RCVD: %s", command,
                              answer)
        self.logger.debug("setAvsamples: SEND: %s\t RCVD: %s", command, answer)

    def setAvsamples(self, avsamples):
        state = self.getState()
        if state == 'RUNNING':
            self.Stop()
        self.StopAdc()
        self._setAvsamples(avsamples)
        self.StartAdc()

    def getPoints(self):
        try:
            command = '?POINTS'
            answer = self.ask(command)
            points = self.extractSimple(answer)
        except Exception as e:
            self.logger.error("getPoints: %s", e)
            raise
        self.logger.debug("getPoints: SEND: %s\t RCVD: %s", command, answer)
        self.logger.debug("getPoints: %s", points)
        return points

    def _setPoints(self, points):
        try:
            command = f'POINTS {points}'
            answer = self.ask(command)
            if answer != 'POINTS ACK\x00':
                raise Exception('setPoints: Wrong acknowledge')
        except Exception as e:
            self.logger.error("setPoints: %s", e)

    def setPoints(self, points):
        state = self.getState()
        if state == 'RUNNING':
            self.Stop()
        self.StopAdc()
        self._setPoints(points)
        self.StartAdc()

    def getTrigDelay(self):
        try:
            command = '?TRIGDELAY'
            self.logger.debug('getTrigDelay: Sending command...')
            answer = self.ask(command)
            trigperiode = self.extractSimple(answer)
        except Exception as e:
            self.logger.error("getTrigDelay: %s", e)
            raise
        self.logger.debug("getTrigDelay: SEND: %s\t RCVD: %s", command, answer)
        self.logger.debug("getTrigDelay: %s", trigperiode)
        return trigperiode

    def _setTrigDelay(self, delay):
        answer = None
        command = f'TRIGDELAY {delay}'
        try:
            answer = self.ask(command)
            if answer != 'TRIGDELAY ACK\x00':
                raise Exception('setTrigDelay: Wrong acknowledge')
        except Exception as e:
            self.logger.error("setTrigDelay: %s", e)
        self.logger.debug("setTrigDelay: SEND: %s\t RCVD: %s", command,
                          answer)

    def setTrigDelay(self, delay):
        """
        This method changes the delay of each trigger
        @param delay: delay in ms.
        """
        state = self.getState()
        if state == 'RUNNING':
            self.Stop()
        self.StopAdc()
        self._setTrigDelay(delay)
        self.StartAdc()

    def getTrigperiod(self):
        try:
            command = '?TRIGPERIODE'
            self.logger.debug('getTrigperiod: Sending command...')
            answer = self.ask(command)
            trigperiode = self.extractSimple(answer)
        except Exception as e:
            self.logger.error("getTrigperiod: %s", e)
            raise
        self.logger.debug("getTrigperiod: SEND: %s\t RCVD: %s", command,
                          answer)
        self.logger.debug("getTrigperiod: %s", trigperiode)
        return trigperiode

    def _setTrigperiod(self, trigperiod):
        answer = None
        command = f'TRIGPERIODE {trigperiod}'

        try:
            answer = self.ask(command)
            if answer != 'TRIGPERIODE ACK\x00':
                raise Exception('setTrigperiod: Wrong acknowledge')
        except Exception as e:
            self.logger.error("setTrigperiod: %s", e)
        self.logger.debug("setTrigperiod: SEND: %s\t RCVD: %s", command,
                          answer)

    def setTrigperiod(self, trigperiod):
        state = self.getState()
        if state == 'RUNNING':
            self.Stop()
        self.StopAdc()
        self._setTrigperiod(trigperiod)
        self.StartAdc()

    def getTrigmode(self):
        try:
            command = '?TRIGMODE'
            self.logger.debug('getTrigmode: Sending command...')
            answer = self.ask(command)
            trigmode = self.extractSimple(answer)
        except Exception as e:
            self.logger.error("getTrigmode: %s", e)
            raise
        self.logger.debug("getTrigmode: SEND: %s\t RCVD: %s", command, answer)
        self.logger.debug("getTrigmode: %s", trigmode)
        return trigmode

    def _setTrigmode(self, trigmode):
        answer = None
        command = f'TRIGMODE {trigmode}'
        try:
            answer = self.ask(command)
            if answer != 'TRIGMODE ACK\x00':
                raise Exception('setTrigmode: Wrong acknowledge')
        except Exception as e:
            self.logger.error("setTrigmode: %s", e)
        self.logger.debug("setTrigmode: SEND: %s\t RCVD: %s", command, answer)

    def setTrigmode(self, trigmode):
        state = self.getState()
        if state == 'RUNNING':
            self.Stop()
        self.StopAdc()
        self._setTrigmode(trigmode)
        self.StartAdc()

    def getSrate(self):
        try:
            command = '?SRATE'
            answer = self.ask(command)
            srate = self.extractSimple(answer)
        except Exception as e:
            self.logger.error("getSrate: %s", e)
            raise
        self.logger.debug("getSrate: SEND: %s\t RCVD: %s", command, answer)
        self.logger.debug("getSrate: %s", srate)
        return srate

    def _setSrate(self, srate):
        answer = None
        command = f'SRATE {srate}'
        try:
            answer = self.ask(command)
            if answer != 'SRATE ACK\x00':
                raise Exception('setSrate: Wrong acknowledge')
        except Exception as e:
            self.logger.error("setSrate: %s", e)
        self.logger.debug("setSrate: SEND: %s\t RCVD: %s", command, answer)

    def setSrate(self, srate):
        state = self.getState()
        if state == 'RUNNING':
            self.Stop()
        self.StopAdc()
        self._setSrate(srate)
        self.StartAdc()

    def getState(self):
        try:
            command = '?STATE'
            answer = self.ask(command)
            state = self.extractSimple(answer)
        except Exception as e:
            self.logger.error("getState: %s", e)
            raise
        self.logger.debug("getState: SEND: %s\t RCVD: %s", command, answer)
        self.logger.debug("getState: %s", state)
        if self.offset_corr_alarm:
            state = "ALARM"
        if self.stateMoving:
            state = "MOVING"
        return state

    def getStatus(self):
        try:
            command = '?STATUS'
            answer = self.ask(command)
            status = self.extractSimple(answer)
        except Exception as e:
            self.logger.error("getStatus: %s", e)
            raise
        self.logger.debug("getStatus: SEND: %s\t RCVD: %s", command, answer)
        self.logger.debug("getStatus: %s", status)
        if self.offset_corr_alarm:
            status = "Current input detected is too high for offset " \
                     "correction for the next Channel(s):\n" + \
                     '\n'.join(self.saturation_list) + \
                     " \nVerify that channel is disconnected before " \
                     "starting the offset correction"
        else:
            status = "Device Status is ON"
        return status

    def getMode(self):
        try:
            command = '?MODE'
            answer = self.ask(command)
            mode = self.extractSimple(answer)
        except Exception as e:
            self.logger.error("getMode: %s", e)
            raise
        self.logger.debug("getMode: SEND: %s\t RCVD: %s", command, answer)
        self.logger.debug("getMode: %s", mode)
        return mode

    def getInfo(self):
        print('Ranges:', self.getRangesAll())
        print('Filters:', self.getFiltersAll())
        print('Invs:', self.getInvsAll())
        print('Offsets:', self.getOffsetsAll())
        print('Ampmodes:', self.getAmpmodesAll())
        print('Avsamples:', self.getAvsamples())

    def Start(self):
        try:
            command = 'START'
            answer = self.ask(command)
            if answer != 'START ACK\x00':
                raise Exception('Start: Wrong acknowledge')
        except Exception as e:
            self.logger.error("Start: %s", e)

    def StartAdc(self):
        try:
            command = 'STARTADC'
            answer = self.ask(command)
            if answer != 'STARTADC ACK\x00':
                raise Exception('StartAdc: Wrong acknowledge')
        except Exception as e:
            self.logger.error("StartAdc: %s", e)

    def StopAdc(self):
        try:
            command = 'STOPADC'
            answer = self.ask(command)
            if answer != 'STOPADC ACK\x00':
                raise Exception('StopAdc: Wrong acknowledge')
        except Exception as e:
            self.logger.error("StopAdc: %s", e)

    def Stop(self):
        answer = None
        command = 'STOP'
        try:
            answer = self.ask(command)
            if answer != 'STOP ACK\x00':
                raise Exception('Stop: Wrong acknowledge')
        except Exception as e:
            self.logger.error("Stop: %s", e)
        self.logger.debug("Stop: SEND: %s\t RCVD: %s", command, answer)

    def sendSetCmd(self, cmd):
        state = self.getState()
        if state == 'RUNNING':
            self.Stop()
        self.StopAdc()
        self.ask(cmd)
        self.StartAdc()

    def clearOffsetCorr(self):
        self.StopAdc()
        for r in RANGES:
            self.ask(f'OFFSETCORR {r} 1 0 2 0 3 0 4 0')
        self.StartAdc()

    def getOffsetCorr(self, range_value, channel):
        """
        @param range_value: Range to use.
        @param channel: channel to use. Starting in 1
        @return: Offset for the channel
        """
        offset = self.ask(f'?OFFSETCORR {range_value} 1 2 3 4')
        offsets = self.extractMultichannel(offset, 2)
        return offsets[channel - 1][1]

    def getOffsetCorrAll(self):
        """
        Get offsets for each range and return a dictionary with an entrance
        for each range.
        """
        offsets = {}
        for r in RANGES:
            command = f'?OFFSETCORR {r}'
            answer = self.ask(command)
            offsets[r] = self.extractMultichannel(answer, 2)
            self.logger.debug("Stop: SEND: %s\t RCVD: %s", command, answer)
        return offsets

    def _setOffsetCorrect(self, rang, chans):
        """
        Is called from setOffsetCorrect,
        @chans is a list os values and chanels
        @rang is a String of range.
        """
        s = " "
        for o in chans:
            for i in o:
                s += f'{i} '
        print(f'Sending command:OFFSETCORR {rang}{s}')
        self.sendSetCmd(f'OFFSETCORR {rang}{s}')

    def setOffsetCorrect(self, values):
        """
        @chans - Diccionary of Channel and values
        @ranges - List of Ranges to loop
        """
        for val in values:
            self._setOffsetCorrect(val, values.get(val))

    def getGainCorrAll(self):
        for r in RANGES:
            self.logger.debug(self.ask(f'?GAINCORR {r}'))

    def resetGainCorr(self, channel):
        for r in RANGES:
            self.logger.debug(self.sendSetCmd(f'GAINCORR {r} {channel} 1'))

    def resetOffsetCorr(self, channel):
        for r in RANGES:
            self.logger.debug(self.sendSetCmd(f'OFFSETCORR {r} {channel} 0'))

    def toggleGainCorrPolarisation(self, channel, factor=-1, relative=1):
        gaincorrs = []
        for r in RANGES:
            value = self.ask(f'?GAINCORR {r}')
            gaincorr = value.strip('\n').strip('\00').split(' ')
            gaincorrs.append(gaincorr)
        self.logger.debug("Initial gaincorr factors:")
        for gc in gaincorrs:
            self.logger.debug(gc)
        state = self.getState()
        if state == 'RUNNING':
            self.Stop()
        self.StopAdc()
        print(f'Channels: {channel}')
        print(f'gaincor: {gaincorrs}')
        if relative == 1:
            for i, r in enumerate(RANGES):
                value = factor * \
                        int(float(gaincorrs[i][2 + 2 * int(channel) - 1]))
                self.ask(f'GAINCORR {r} {channel} {value}')
                time.sleep(0.2)
        else:
            for i, r in enumerate(RANGES):
                value = factor * \
                        abs(int(float(gaincorrs[i][2 + 2 * int(channel) - 1])))

                self.ask(f'GAINCORR {r} {channel} {value}')

        self.StartAdc()
        gaincorrs = []
        for r in RANGES:
            value = self.ask(f'?GAINCORR {r}')
            gaincorr = value.strip('\n').strip('\00').split(' ')
            gaincorrs.append(gaincorr)
        self.logger.debug("Final gaincorr factors:")
        for gc in gaincorrs:
            self.logger.debug(gc)

    def loadConfig(self, loadfile):
        cmd = []
        myfile = open(loadfile, 'r')
        mylogstring = myfile.readlines()
        for i in range(0, 6):
            mystring = mylogstring[i].strip('\n').split(',')
            cmd.append(f"{mystring[0]} 1 {mystring[1]} 2 {mystring[2]} "
                       f"3 {mystring[3]} 4 {mystring[4]}")
        for i in range(6, len(mylogstring)):
            mystring = mylogstring[i].strip('\n').split(',')
            cmd.append(f"{mystring[0]} {mystring[1]} 1 {mystring[2]} "
                       f"2 {mystring[3]} 3 {mystring[4]} 4 {mystring[5]}")

        self.logger.debug("Loading config to EM:")
        for c in cmd:
            self.sendSetCmd(c)

    def _dumpConfig(self):
        mylogstring = []
        mystring = self.ask('?RANGE').strip('\x00').split(' ')
        mylogstring.append(
            "RANGE,%s,%s,%s,%s\n" %
            (mystring[2], mystring[4], mystring[6], mystring[8]))
        mystring = self.ask('?FILTER').strip('\x00').split(' ')
        mylogstring.append(
            "FILTER,%s,%s,%s,%s\n" %
            (mystring[2], mystring[4], mystring[6], mystring[8]))
        mystring = self.ask('?INV').strip('\x00').split(' ')
        mylogstring.append(
            "INV,%s,%s,%s,%s\n" %
            (mystring[2], mystring[4], mystring[6], mystring[8]))
        mystring = self.ask('?OFFSET').strip('\x00').split(' ')
        mylogstring.append(
            "OFFSET,%s,%s,%s,%s\n" %
            (mystring[2], mystring[4], mystring[6], mystring[8]))
        mystring = self.ask('?ENABLE').strip('\x00').split(' ')
        mylogstring.append(
            "ENABLE,%s,%s,%s,%s\n" %
            (mystring[2], mystring[4], mystring[6], mystring[8]))
        mystring = self.ask('?AMPMODE').strip('\x00').split(' ')
        mylogstring.append(
            "AMPMODE,%s,%s,%s,%s\n" %
            (mystring[2], mystring[4], mystring[6], mystring[8]))
        for r in RANGES:
            mystring = self.ask('?OFFSETCORR %s' % r).strip('\x00').split(' ')
            mylogstring.append(
                "OFFSETCORR,%s,%s,%s,%s,%s\n" %
                (r, mystring[3], mystring[5], mystring[7], mystring[9]))
        for r in RANGES:
            mystring = self.ask('?GAINCORR %s' % r).strip('\x00').split(' ')
            mylogstring.append(
                "GAINCORR,%s,%s,%s,%s,%s\n" %
                (r, mystring[3], mystring[5], mystring[7], mystring[9]))
        return mylogstring

    def dumpConfig(self, dumpfile):
        mylogstring = self._dumpConfig()
        myfile = open(dumpfile, 'w')
        self.logger.debug("Dumping config to file: %s" % dumpfile)
        for line in mylogstring:
            self.logger.debug(line.strip('\n'))
            myfile.write(line)

    def dumpDefaultConfig(self):
        self.dumpConfig('./%s.dump' % self.host)

    def loadDefaultConfig(self):
        self.loadConfig('./%s.dump' % self.host)

    def checkAgainstDumpedConfig(self, dumpfile):
        mylogstring = self._dumpConfig()
        myfile = open(dumpfile, 'r')
        mydumpedstring = myfile.readlines()
        missmatches = 0
        self.logger.debug(
            "Comparing config of em %s with dumpfile %s..." %
            (self.host, dumpfile))
        for i in range(0, len(mylogstring)):
            if mylogstring[i] != mydumpedstring[i]:
                self.logger.debug(
                    "Current config and dumped config missmatch:")
                self.logger.debug("Current: %s" % mylogstring[i].strip('\n'))
                self.logger.debug(
                    "Dump file: %s" %
                    mydumpedstring[i].strip('\n'))
                missmatches = missmatches + 1
        self.logger.debug(
            "Comparison finished. Number of missmatches:%s" %
            missmatches)

    def checkAgainstDefaultDumpedConfig(self):
        self.checkAgainstDumpedConfig('./%s.dump' % self.host)


if __name__ == "__main__":
    # TWO BASIC PARAMETERS, unit address and channel
    # Substitute ask by ask2 in order to use savechain method for debugging
    # without hw

    DftLogFormat = '%(threadName)-14s %(levelname)-8s %(asctime)s %(name)s: ' \
                   '%(message)s'
    # logging.basicConfig(filename='filenameforlogs.log',format=DftLogFormat)
    myFormat = logging.Formatter(DftLogFormat)
    handler = logging.handlers.RotatingFileHandler(
        'LibTestingErrors', maxBytes=10240, backupCount=5)
    handler.setFormatter(myFormat)
    myalbaem = AlbaEm('elem01r42s009')
    myalbaem.logger.addHandler(handler)
