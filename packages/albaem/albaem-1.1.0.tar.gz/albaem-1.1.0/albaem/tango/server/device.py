import _thread
import math
import logging
import logging.handlers
import time

from tango import DevState, Database, AttrQuality, DeviceProxy
from tango.server import Device, attribute, command, device_property

from ...core import AlbaEm


class PyAlbaEm(Device):
    AlbaEmName = device_property(dtype=str)
    LogFileName = device_property(dtype=str, default_value="")

    # TODO: Evaluate if we want to implement.
    # DynamicAttributes = device_property(dtype=[str], default_value="")

    def init_device(self):
        super().init_device()
        # used to reduce the number of readings from electrometer.
        self.AllRanges = [0, 0, 0, 0]
        self._allMeasures = [0, 0, 0, 0]
        list_values = []
        self.offset_percentage_ch1 = 0
        self.offset_percentage_ch2 = 0
        self.offset_percentage_ch3 = 0
        self.offset_percentage_ch4 = 0
        # @note: Not too clear the difference between getLogger() and Logger()
        self.my_logger = logging.getLogger('albaEM DS')

        list_attr = ("offset_percentage_ch1", "offset_percentage_ch2",
                     "offset_percentage_ch3", "offset_percentage_ch4")

        for i in list_attr:
            value = self.get_attribute_memorized_value(i)
            if value is None:
                value = 0
            list_values.append(int(value))
        self._offsetPercentages = list_values

        self.dictRanges = {'1mA': 1e-3, '100uA': 1e-4, '10uA': 1e-5,
                           '1uA': 1e-6,
                           '100nA': 1e-7, '10nA': 1e-8, '1nA': 1e-9,
                           '100pA': 1e-10}

        # @todo: check why memorized is not working
        self._channelsNames = ['I1', 'I2', 'I3', 'I4']
        self.__numOfPoints = 0
        self.AduToVoltConstant = 1818
        self.attr_I1_read = None
        self.attr_I2_read = None
        self.attr_I3_read = None
        self.attr_I4_read = None

        try:
            self.set_state(DevState.ON)
            self.AlbaElectr = AlbaEm(self.AlbaEmName)

            if self.LogFileName != "" or \
                    self.LogFileName is None or \
                    self.LogFileName == []:
                DftLogFormat = \
                    '%(threadName)-14s %(levelname)-8s %(asctime)s ' \
                    '%(name)s: %(message)s'
                myFormat = logging.Formatter(DftLogFormat)
                # self.my_logger = logging.getLogger('albaEM DS') #@note: Not
                # too clear the difference between getLogger() and Logger()
                self.my_logger.setLevel(logging.DEBUG)
                handler = \
                    logging.handlers.RotatingFileHandler(self.LogFileName,
                                                         maxBytes=10240000,
                                                         backupCount=5)
                handler.setFormatter(myFormat)
                self.my_logger.addHandler(handler)

                self.AlbaElectr.logger.addHandler(handler)

            self.AlbaElectr.setEnablesAll('YES')
            state = self.AlbaElectr.getState()
            self.my_logger.info('State at init_device: %s', state)
            self.getAllRanges()

        except Exception as e:
            self.set_state(DevState.FAULT)
            self.my_logger.error("Exception in init_device: %s", e)

    def delete_device(self):
        print("[Device delete_device method] for device", self.get_name())

    def get_attribute_memorized_value(self, attr_name):
        w_val = None
        db = Database()
        properties = db.get_device_attribute_property(
            self.get_name(), attr_name)
        attr_properties = properties[attr_name]
        try:
            w_val = attr_properties["__value"][0]
        except KeyError:
            msg = 'Unable to retrieve memorized value of attr: %s' % attr_name
            self.my_logger.warning(msg)
        return w_val

    # def always_executed_hook(self):
    #     self.dev_state()

    def dev_state(self):
        state = self.AlbaElectr.getState()

        if state == 'ON':
            return DevState.ON
        elif state == 'RUNNING':
            return DevState.RUNNING
        elif state == 'IDLE':
            return DevState.STANDBY
        elif state == 'ALARM':
            return DevState.ALARM
        elif state == 'MOVING':
            return DevState.MOVING
        else:
            self.my_logger.error('Unknown state %s', state)

    @attribute(dtype=float)
    def I1(self):
        try:
            self.attr_I1_read = float(self.AlbaElectr.getMeasure('1'))
            return self.attr_I1_read
        except Exception as e:
            self.set_state(DevState.FAULT)
            self.my_logger.error("Exception in read I1: %s", e)

    @attribute(dtype=float)
    def I2(self):
        try:
            self.attr_I2_read = float(self.AlbaElectr.getMeasure('2'))
            return self.attr_I2_read
        except Exception as e:
            self.set_state(DevState.FAULT)
            self.my_logger.error("Exception in read I2: %s", e)

    @attribute(dtype=float)
    def I3(self):
        try:
            self.attr_I3_read = float(self.AlbaElectr.getMeasure('3'))
            return self.attr_I3_read
        except Exception as e:
            self.set_state(DevState.FAULT)
            self.my_logger.error("Exception in read I3: %s", e)

    @attribute(dtype=float)
    def I4(self):
        try:
            self.attr_I4_read = float(self.AlbaElectr.getMeasure('4'))
            return self.attr_I4_read
        except Exception as e:
            self.set_state(DevState.FAULT)
            self.my_logger.error("Exception in read I4: %s", e)

    @attribute(dtype=float)
    def InstantI1(self):
        try:
            return float(self.AlbaElectr.getInstantMeasure('1'))
        except Exception as e:
            self.set_state(DevState.FAULT)
            self.my_logger.error("Exception in read InstantI1: %s", e)

    @attribute(dtype=float)
    def InstantI2(self):
        try:
            return float(self.AlbaElectr.getInstantMeasure('2'))
        except Exception as e:
            self.set_state(DevState.FAULT)
            self.my_logger.error("Exception in read InstantI2: %s", e)

    @attribute(dtype=float)
    def InstantI3(self):
        try:
            return float(self.AlbaElectr.getInstantMeasure('3'))
        except Exception as e:
            self.set_state(DevState.FAULT)
            self.my_logger.error("Exception in read InstantI3: %s", e)

    @attribute(dtype=float)
    def InstantI4(self):
        try:
            return float(self.AlbaElectr.getInstantMeasure('4'))
        except Exception as e:
            self.set_state(DevState.FAULT)
            self.my_logger.error("Exception in read InstantI4: %s", e)

    @attribute(dtype=[float], max_dim_x=4)
    def AllChannels(self):
        try:
            measures = self.AlbaElectr.getMeasuresAll()[0]
            for i, value in enumerate(measures):
                self._allMeasures[i] = float(value[1])
            return self._allMeasures
        except Exception as e:
            self.set_state(DevState.FAULT)
            self.my_logger.error("Exception in read_AllChannels: %s", e)

    @attribute(dtype=[float],  max_dim_x=4)
    def LastValues(self):
        try:
            _lastValues = [0, 0, 0, 0]
            lastValues = self.AlbaElectr.getLdata()
            if lastValues is not None:
                for i, value in enumerate(lastValues[0]):
                    _lastValues[i] = float(value[1])
                return _lastValues

            else:
                self.my_logger.error('lastValues = None !!')
        except Exception:
            try:
                measures = self.AlbaElectr.getMeasuresAll()[0]
                for i, value in enumerate(measures):
                    _lastValues[i] = float(value[1])
                return _lastValues
            except Exception as e:
                self.set_state(DevState.FAULT)
                self.my_logger.error("Exception in read_LastValues: %s", e)
                self.my_logger.error("lastValues: %s", str(_lastValues))

    @attribute(dtype=str)
    def range_ch1(self):
        try:
            rgs = self.AlbaElectr.getRanges(['1'])
            attr_range_ch1_read = rgs[0]
            value = attr_range_ch1_read[1]
            self.AllRanges[0] = value
            quality = AttrQuality.ATTR_VALID
            if self.attr_I1_read is not None:
                quality = self.checkRanges(self.attr_I1_read, 0)

            return value, time.time(), quality
        except Exception as e:
            self.set_state(DevState.FAULT)
            self.my_logger.error("Exception in read_range_ch1: %s", e)

    @range_ch1.setter
    def range_ch1(self, value):
        print("Attribute value = ", value)

        #    Add your own code here
        self.AlbaElectr.setRanges([['1', value]])
        self.AllRanges[0] = value
        print(str(self.AlbaElectr.getRanges(['1'])))

    @attribute(dtype=str)
    def range_ch2(self):
        try:
            rgs = self.AlbaElectr.getRanges(['2'])
            attr_range_ch2_read = rgs[0]
            value = attr_range_ch2_read[1]
            self.AllRanges[1] = value
            quality = AttrQuality.ATTR_VALID
            if self.attr_I2_read is not None:
                quality = self.checkRanges(self.attr_I2_read, 1)
            return value, time.time(), quality
        except Exception as e:
            self.set_state(DevState.FAULT)
            self.my_logger.error("Exception in read_range_ch2: %s", e)

    @range_ch2.setter
    def range_ch2(self, value):
        print("Attribute value = ", value)

        #    Add your own code here
        self.AlbaElectr.setRanges([['2', value]])
        self.AllRanges[1] = value
        print(str(self.AlbaElectr.getRanges(['2'])))

    @attribute(dtype=str)
    def range_ch3(self):
        try:
            rgs = self.AlbaElectr.getRanges(['3'])
            attr_range_ch3_read = rgs[0]
            value = attr_range_ch3_read[1]
            self.AllRanges[2] = value
            quality = AttrQuality.ATTR_VALID
            if self.attr_I3_read is not None:
                quality = self.checkRanges(self.attr_I3_read, 2)
            return value, time.time(), quality
        except Exception as e:
            self.set_state(DevState.FAULT)
            self.my_logger.error("Exception in read_range_ch3: %s", e)

    @range_ch3.setter
    def range_ch3(self, value):
        print("Attribute value = ", value)

        #    Add your own code here
        self.AlbaElectr.setRanges([['3', value]])
        self.AllRanges[2] = value
        print(str(self.AlbaElectr.getRanges(['3'])))

    @attribute(dtype=str)
    def range_ch4(self):
        try:
            rgs = self.AlbaElectr.getRanges(['4'])
            attr_range_ch4_read = rgs[0]
            value = attr_range_ch4_read[1]
            self.AllRanges[3] = value
            quality = AttrQuality.ATTR_VALID
            if self.attr_I4_read is not None:
                quality = self.checkRanges(self.attr_I4_read, 3)
            return value, time.time(), quality
        except Exception as e:
            self.set_state(DevState.FAULT)
            self.my_logger.error("Exception in read_range_ch4: %s", e)

    @range_ch4.setter
    def range_ch4(self, value):
        print("Attribute value = ", value)

        #    Add your own code here
        self.AlbaElectr.setRanges([['4', value]])
        self.AllRanges[3] = value
        print(str(self.AlbaElectr.getRanges(['4'])))

    @attribute(dtype=[str],  max_dim_x=4,
               description="You must introduce the four ranges to write.\n"
                           "Example of writing value: 1mA 1mA 1uA 100uA")
    def Ranges(self):
        try:
            self.getAllRanges()
            return self.AllRanges
        except Exception as e:
            self.set_state(DevState.FAULT)
            self.my_logger.error("Exception in read_Ranges: %s", e)

    @Ranges.setter
    def Ranges(self, values):
        ranges = []
        for i, value in enumerate(values):
            r = [str(i + 1), value]
            ranges.append(r)
            self.AllRanges[i] = value
        self.AlbaElectr.setRanges(ranges)
        print(str(self.AlbaElectr.getRanges(['1', '2', '3', '4'])))

    @attribute(dtype=bool)
    def AutoRange_ch1(self):
        try:
            autoR = self.AlbaElectr.getAutoRange(['1'])
            if autoR[0][1] == 'YES':
                return True
            elif autoR[0][1] == 'NO':
                return False
            else:
                raise Exception('read_AutoRange_ch1: Wrong reading')
        except Exception as e:
            self.set_state(DevState.FAULT)
            self.my_logger.error("Exception in read_AutoRange_ch1: %s", e)

    @AutoRange_ch1.setter
    def AutoRange_ch1(self, value):
        print("Attribute value = ", value)
        if value:
            self.AlbaElectr.setAutoRange([['1', 'YES']])
        else:
            self.AlbaElectr.setAutoRange([['1', 'NO']])
        print(str(self.AlbaElectr.getAutoRange(['1'])))

    @attribute(dtype=bool)
    def AutoRange_ch2(self):
        try:
            autoR = self.AlbaElectr.getAutoRange(['2'])
            if autoR[0][1] == 'YES':
                return True
            elif autoR[0][1] == 'NO':
                return False
            else:
                raise Exception('read_AutoRange_ch2: Wrong reading')
        except Exception as e:
            self.set_state(DevState.FAULT)
            self.my_logger.error("Exception in read_AutoRange_ch2: %s", e)

    @AutoRange_ch2.setter
    def AutoRange_ch2(self, value):
        print("Attribute value = ", value)
        if value:
            self.AlbaElectr.setAutoRange([['2', 'YES']])
        else:
            self.AlbaElectr.setAutoRange([['2', 'NO']])
        print(str(self.AlbaElectr.getAutoRange(['2'])))

    @attribute(dtype=bool)
    def AutoRange_ch3(self):
        try:
            autoR = self.AlbaElectr.getAutoRange(['3'])
            if autoR[0][1] == 'YES':
                return True
            elif autoR[0][1] == 'NO':
                return False
            else:
                raise Exception('read_AutoRange_ch3: Wrong reading')
        except Exception as e:
            self.set_state(DevState.FAULT)
            self.my_logger.error("Exception in read_AutoRange_ch3: %s", e)

    @AutoRange_ch3.setter
    def AutoRange_ch3(self, value):
        print("Attribute value = ", value)
        if value:
            self.AlbaElectr.setAutoRange([['3', 'YES']])
        else:
            self.AlbaElectr.setAutoRange([['3', 'NO']])
        print(str(self.AlbaElectr.getAutoRange(['3'])))

    @attribute(dtype=bool)
    def AutoRange_ch4(self):
        try:
            autoR = self.AlbaElectr.getAutoRange(['4'])
            if autoR[0][1] == 'YES':
                return True
            elif autoR[0][1] == 'NO':
                return False
            else:
                raise Exception('read_AutoRange_ch4: Wrong reading')
        except Exception as e:
            self.set_state(DevState.FAULT)
            self.my_logger.error("Exception in read_AutoRange_ch4: %s", e)

    @AutoRange_ch4.setter
    def AutoRange_ch4(self, value):
        print("Attribute value = ", value)
        if value:
            self.AlbaElectr.setAutoRange([['4', 'YES']])
        else:
            self.AlbaElectr.setAutoRange([['4', 'NO']])
        print(str(self.AlbaElectr.getAutoRange(['4'])))

    @attribute(dtype=int)
    def AutoRangeMin_ch1(self):
        try:
            attr_AutoRangeMin_read = self.AlbaElectr.getAutoRangeMin(['1'])

            return int(attr_AutoRangeMin_read[0][1])
        except Exception as e:
            self.set_state(DevState.FAULT)
            self.my_logger.error("Exception in read_AutoRangeMin_ch1: %s", e)

    @AutoRangeMin_ch1.setter
    def AutoRangeMin_ch1(self, value):
        print("Attribute value = ", value)

        self.AlbaElectr.setAutoRangeMin([['1', value]])
        print(str(self.AlbaElectr.getAutoRangeMin(['1'])))

    @attribute(dtype=int)
    def AutoRangeMin_ch2(self):
        try:
            attr_AutoRangeMin_read = self.AlbaElectr.getAutoRangeMin(['2'])

            return int(attr_AutoRangeMin_read[0][1])
        except Exception as e:
            self.set_state(DevState.FAULT)
            self.my_logger.error("Exception in read_AutoRangeMin_ch2: %s", e)

    @AutoRangeMin_ch2.setter
    def AutoRangeMin_ch2(self, value):
        print("Attribute value = ", value)

        self.AlbaElectr.setAutoRangeMin([['2', value]])
        print(str(self.AlbaElectr.getAutoRangeMin(['2'])))

    @attribute(dtype=int)
    def AutoRangeMin_ch3(self):
        try:
            attr_AutoRangeMin_read = self.AlbaElectr.getAutoRangeMin(['3'])

            return int(attr_AutoRangeMin_read[0][1])
        except Exception as e:
            self.set_state(DevState.FAULT)
            self.my_logger.error("Exception in read_AutoRangeMin_ch3: %s", e)

    @AutoRangeMin_ch3.setter
    def AutoRangeMin_ch3(self, value):
        print("Attribute value = ", value)

        self.AlbaElectr.setAutoRangeMin([['3', value]])
        print(str(self.AlbaElectr.getAutoRangeMin(['3'])))

    @attribute(dtype=int)
    def AutoRangeMin_ch4(self):
        try:
            attr_AutoRangeMin_read = self.AlbaElectr.getAutoRangeMin(['4'])

            return int(attr_AutoRangeMin_read[0][1])
        except Exception as e:
            self.set_state(DevState.FAULT)
            self.my_logger.error("Exception in read_AutoRangeMin_ch4: %s", e)

    @AutoRangeMin_ch4.setter
    def AutoRangeMin_ch4(self, value):
        print("Attribute value = ", value)

        self.AlbaElectr.setAutoRangeMin([['4', value]])
        print(str(self.AlbaElectr.getAutoRangeMin(['4'])))

    @attribute(dtype=int)
    def AutoRangeMax_ch1(self):
        try:
            attr_AutoRangeMax_read = self.AlbaElectr.getAutoRangeMax(['1'])

            return int(attr_AutoRangeMax_read[0][1])
        except Exception as e:
            self.set_state(DevState.FAULT)
            self.my_logger.error("Exception in read_AutoRangeMax_ch1: %s", e)

    @AutoRangeMax_ch1.setter
    def AutoRangeMax_ch1(self, value):
        print("Attribute value = ", value)
        self.AlbaElectr.setAutoRangeMax([['1', value]])

        print(str(self.AlbaElectr.getAutoRangeMax(['1'])))

    @attribute(dtype=int)
    def AutoRangeMax_ch2(self):
        try:
            attr_AutoRangeMax_read = self.AlbaElectr.getAutoRangeMax(['2'])

            return int(attr_AutoRangeMax_read[0][1])
        except Exception as e:
            self.set_state(DevState.FAULT)
            self.my_logger.error("Exception in read_AutoRangeMax_ch2: %s", e)

    @AutoRangeMax_ch2.setter
    def AutoRangeMax_ch2(self, value):
        print("Attribute value = ", value)
        self.AlbaElectr.setAutoRangeMax([['2', value]])

        print(str(self.AlbaElectr.getAutoRangeMax(['2'])))

    @attribute(dtype=int)
    def AutoRangeMax_ch3(self):
        try:
            attr_AutoRangeMax_read = self.AlbaElectr.getAutoRangeMax(['3'])

            return int(attr_AutoRangeMax_read[0][1])
        except Exception as e:
            self.set_state(DevState.FAULT)
            self.my_logger.error("Exception in read_AutoRangeMax_ch3: %s", e)

    @AutoRangeMax_ch3.setter
    def AutoRangeMax_ch3(self, value):
        print("Attribute value = ", value)
        self.AlbaElectr.setAutoRangeMax([['3', value]])

        print(str(self.AlbaElectr.getAutoRangeMax(['3'])))

    @attribute(dtype=int)
    def AutoRangeMax_ch4(self):
        try:
            attr_AutoRangeMax_read = self.AlbaElectr.getAutoRangeMax(['4'])

            return int(attr_AutoRangeMax_read[0][1])
        except Exception as e:
            self.set_state(DevState.FAULT)
            self.my_logger.error("Exception in read_AutoRangeMax_ch4: %s", e)

    @AutoRangeMax_ch4.setter
    def AutoRangeMax_ch4(self, value):
        print("Attribute value = ", value)
        self.AlbaElectr.setAutoRangeMax([['4', value]])

        print(str(self.AlbaElectr.getAutoRangeMax(['4'])))

    @attribute(dtype=str)
    def filter_ch1(self):
        try:
            fltr = self.AlbaElectr.getFilters(['1'])
            attr_filter_ch1_read = fltr[0]
            return attr_filter_ch1_read[1]
        except Exception as e:
            self.set_state(DevState.FAULT)
            self.my_logger.error("Exception in read_filter_ch1: %s", e)

    @filter_ch1.setter
    def filter_ch1(self, value):
        print("Attribute value = ", value)

        self.AlbaElectr.setFilters([['1', value]])
        print(str(self.AlbaElectr.getFilters(['1'])))

    @attribute(dtype=str)
    def filter_ch2(self):
        try:
            fltr = self.AlbaElectr.getFilters(['2'])
            attr_filter_ch1_read = fltr[0]
            return attr_filter_ch1_read[1]
        except Exception as e:
            self.set_state(DevState.FAULT)
            self.my_logger.error("Exception in read_filter_ch2: %s", e)

    @filter_ch2.setter
    def filter_ch2(self, value):
        print("Attribute value = ", value)

        self.AlbaElectr.setFilters([['2', value]])
        print(str(self.AlbaElectr.getFilters(['2'])))

    @attribute(dtype=str)
    def filter_ch3(self):
        try:
            fltr = self.AlbaElectr.getFilters(['3'])
            attr_filter_ch1_read = fltr[0]
            return attr_filter_ch1_read[1]
        except Exception as e:
            self.set_state(DevState.FAULT)
            self.my_logger.error("Exception in read_filter_ch3: %s", e)

    @filter_ch3.setter
    def filter_ch3(self, value):
        print("Attribute value = ", value)

        self.AlbaElectr.setFilters([['3', value]])
        print(str(self.AlbaElectr.getFilters(['3'])))

    @attribute(dtype=str)
    def filter_ch4(self):
        try:
            fltr = self.AlbaElectr.getFilters(['4'])
            attr_filter_ch1_read = fltr[0]
            return attr_filter_ch1_read[1]
        except Exception as e:
            self.set_state(DevState.FAULT)
            self.my_logger.error("Exception in read_filter_ch4: %s", e)

    @filter_ch4.setter
    def filter_ch4(self, value):
        print("Attribute value = ", value)

        self.AlbaElectr.setFilters([['4', value]])
        print(str(self.AlbaElectr.getFilters(['4'])))

    @attribute(dtype=[str],  max_dim_x=4,
               description="You must introduce the four filters to write.\n"
                           "Example of writing value: 1 10 100 NO ")
    def Filters(self):
        try:
            fltrs = self.AlbaElectr.getFiltersAll()
            fltrsList = []
            for i in fltrs:
                fltrsList.append(i[1])
            return fltrsList
        except Exception as e:
            self.set_state(DevState.FAULT)
            self.my_logger.error("Exception in read_Filters: %s", e)

    @Filters.setter
    def Filters(self, values):
        print("Attribute value = ", values)
        filters = []
        for i, value in enumerate(values):
            v = [str(i+1), value]
            filters.append(v)
        self.AlbaElectr.setFilters(filters)
        print(str(self.AlbaElectr.getFiltersAll()))

    @attribute(dtype=str)
    def aInversion_ch1(self):
        try:
            aInv = self.AlbaElectr.getInvs(['1'])
            return aInv[0][1]
        except Exception as e:
            self.set_state(DevState.FAULT)
            self.my_logger.error("Exception in read_aInversion_ch1: %s", e)

    @aInversion_ch1.setter
    def aInversion_ch1(self, value):
        print("Attribute value = ", value)
        self.AlbaElectr.setInvs([['1', value]])
        print(str(self.AlbaElectr.getInvs(['1'])))

    @attribute(dtype=str)
    def aInversion_ch2(self):
        try:
            aInv = self.AlbaElectr.getInvs(['2'])
            return aInv[0][1]
        except Exception as e:
            self.set_state(DevState.FAULT)
            self.my_logger.error("Exception in read_aInversion_ch2: %s", e)

    @aInversion_ch2.setter
    def aInversion_ch2(self, value):
        print("Attribute value = ", value)
        self.AlbaElectr.setInvs([['2', value]])
        print(str(self.AlbaElectr.getInvs(['2'])))

    @attribute(dtype=str)
    def aInversion_ch3(self):
        try:
            aInv = self.AlbaElectr.getInvs(['3'])
            return aInv[0][1]
        except Exception as e:
            self.set_state(DevState.FAULT)
            self.my_logger.error("Exception in read_aInversion_ch3: %s", e)

    @aInversion_ch3.setter
    def aInversion_ch3(self, value):
        print("Attribute value = ", value)
        self.AlbaElectr.setInvs([['3', value]])
        print(str(self.AlbaElectr.getInvs(['3'])))

    @attribute(dtype=str)
    def aInversion_ch4(self):
        try:
            aInv = self.AlbaElectr.getInvs(['4'])
            return aInv[0][1]
        except Exception as e:
            self.set_state(DevState.FAULT)
            self.my_logger.error("Exception in read_aInversion_ch4: %s", e)

    @aInversion_ch4.setter
    def aInversion_ch4(self, value):
        print("Attribute value = ", value)
        self.AlbaElectr.setInvs([['4', value]])
        print(str(self.AlbaElectr.getInvs(['4'])))

    @attribute(dtype=[str],  max_dim_x=4,
               description="You must introduce the four analog inversions in "
                           "order to write. First one corresponds to"
                           " first channel and so on.\n"
                           "Example: NO,NO,YES,YES")
    def aInversions(self):
        try:
            aInvs = self.AlbaElectr.getInvsAll()
            aInvsList = []
            for i in aInvs:
                aInvsList.append(i[1])
            return aInvsList
        except Exception as e:
            self.set_state(DevState.FAULT)
            self.my_logger.error("Exception in read_aInversions: %s", e)

    @aInversions.setter
    def aInversions(self, values):
        print("Attribute value = ", values)
        invs = []
        for i, value in enumerate(values):
            v = [str(i + 1), value]
            invs.append(v)

        self.AlbaElectr.setInvs(invs)
        print(str(self.AlbaElectr.getInvsAll()))

    @attribute(dtype=str)
    def dInversion_ch1(self):
        try:
            dInv = self.AlbaElectr.getDInvs(['1'])
            return dInv[0][1]
        except Exception as e:
            self.set_state(DevState.FAULT)
            self.my_logger.error("Exception in read_dInversion_ch1: %s", e)

    @dInversion_ch1.setter
    def dInversion_ch1(self, value):
        print("Attribute value = ", value)
        self.AlbaElectr.setDInvs([['1', value]])
        print(str(self.AlbaElectr.getDInvs(['1'])))

    @attribute(dtype=str)
    def dInversion_ch2(self):
        try:
            dInv = self.AlbaElectr.getDInvs(['2'])
            return dInv[0][1]
        except Exception as e:
            self.set_state(DevState.FAULT)
            self.my_logger.error("Exception in read_dInversion_ch2: %s", e)

    @dInversion_ch2.setter
    def dInversion_ch2(self, value):
        print("Attribute value = ", value)
        self.AlbaElectr.setDInvs([['2', value]])
        print(str(self.AlbaElectr.getDInvs(['2'])))

    @attribute(dtype=str)
    def dInversion_ch3(self):
        try:
            dInv = self.AlbaElectr.getDInvs(['3'])
            return dInv[0][1]
        except Exception as e:
            self.set_state(DevState.FAULT)
            self.my_logger.error("Exception in read_dInversion_ch3: %s", e)

    @dInversion_ch3.setter
    def dInversion_ch3(self, value):
        print("Attribute value = ", value)
        self.AlbaElectr.setDInvs([['3', value]])
        print(str(self.AlbaElectr.getDInvs(['3'])))

    @attribute(dtype=str)
    def dInversion_ch4(self):
        try:
            dInv = self.AlbaElectr.getDInvs(['4'])
            return dInv[0][1]
        except Exception as e:
            self.set_state(DevState.FAULT)
            self.my_logger.error("Exception in read_dInversion_ch4: %s", e)

    @dInversion_ch4.setter
    def dInversion_ch4(self, value):
        print("Attribute value = ", value)
        self.AlbaElectr.setDInvs([['4', value]])
        print(str(self.AlbaElectr.getDInvs(['4'])))

    @attribute(dtype=[str],  max_dim_x=4,
               description="You must introduce the four digital inversions in "
                           "order to write. First one corresponds to"
                           " first channel and so on.\n"
                           "Example: NO,NO,YES,YES"
               )
    def dInversions(self):
        try:
            dInvs = self.AlbaElectr.getDInvsAll()
            dInvsList = []
            for i in dInvs:
                dInvsList.append(i[1])
            return dInvsList
        except Exception as e:
            self.set_state(DevState.FAULT)
            self.my_logger.error("Exception in read_dInversions: %s", e)

    @dInversions.setter
    def dInversions(self, values):
        print("Attribute value = ", values)
        invs = []
        for i, value in enumerate(values):
            v = [str(i+1), value]
            invs.append(v)

        self.AlbaElectr.setDInvs(invs)
        print(str(self.AlbaElectr.getDInvsAll()))

    @attribute(dtype=float)
    def offset_ch1(self):
        try:
            offset = (self.dictRanges[self.AllRanges[0]]
                      * self._offsetPercentages[0]) / 100.0
            return offset
        except Exception as e:
            self.set_state(DevState.FAULT)
            self.my_logger.error("Exception in read_offset_ch1: %s", e)

    @attribute(dtype=float)
    def offset_ch2(self):
        try:
            offset = (self.dictRanges[self.AllRanges[1]]
                      * self._offsetPercentages[1]) / 100.0
            return offset
        except Exception as e:
            self.set_state(DevState.FAULT)
            self.my_logger.error("Exception in read_offset_ch2: %s", e)

    @attribute(dtype=float)
    def offset_ch3(self):
        try:
            offset = (self.dictRanges[self.AllRanges[2]]
                      * self._offsetPercentages[2]) / 100.0
            return offset
        except Exception as e:
            self.set_state(DevState.FAULT)
            self.my_logger.error("Exception in read_offset_ch3: %s", e)

    @attribute(dtype=float)
    def offset_ch4(self):
        try:
            offset = (self.dictRanges[self.AllRanges[3]]
                      * self._offsetPercentages[3]) / 100.0
            return offset
        except Exception as e:
            self.set_state(DevState.FAULT)
            self.my_logger.error("Exception in read_offset_ch4: %s", e)

    @attribute(dtype=float, memorized=True)
    def offset_percentage_ch1(self):
        try:
            return self._offsetPercentages[0]
        except Exception as e:
            self.set_state(DevState.FAULT)
            self.my_logger.error(
                "Exception in read_offset_percentage_ch1: %s", e)

    @offset_percentage_ch1.setter
    def offset_percentage_ch1(self, value):
        print("Attribute value = ", value)
        self._offsetPercentages[0] = value
        self.info_stream('!!!Writing offset percentage ch1 done!!!')
        offset = value / 100.0
        _thread.start_new_thread(self.changeOffsets, ([1], offset))

    @attribute(dtype=float, memorized=True)
    def offset_percentage_ch2(self):
        try:
            return self._offsetPercentages[1]
        except Exception as e:
            self.set_state(DevState.FAULT)
            self.my_logger.error(
                "Exception in read_offset_percentage_ch2: %s", e)

    @offset_percentage_ch2.setter
    def offset_percentage_ch2(self, value):
        print("Attribute value = ", value)
        self._offsetPercentages[1] = value
        self.info_stream('!!!Writing offset percentage ch2 done!!!')
        offset = value / 100.0
        _thread.start_new_thread(self.changeOffsets, ([2], offset))

    @attribute(dtype=float, memorized=True)
    def offset_percentage_ch3(self):
        try:
            return self._offsetPercentages[2]
        except Exception as e:
            self.set_state(DevState.FAULT)
            self.my_logger.error(
                "Exception in read_offset_percentage_ch3: %s", e)

    @offset_percentage_ch3.setter
    def offset_percentage_ch3(self, value):
        print("Attribute value = ", value)
        self._offsetPercentages[2] = value
        self.info_stream('!!!Writing offset percentage ch3 done!!!')
        offset = value / 100.0
        _thread.start_new_thread(self.changeOffsets, ([3], offset))

    @attribute(dtype=float, memorized=True)
    def offset_percentage_ch4(self):
        try:
            return self._offsetPercentages[3]
        except Exception as e:
            self.set_state(DevState.FAULT)
            self.my_logger.error(
                "Exception in read_offset_percentage_ch4: %s", e)

    @offset_percentage_ch4.setter
    def offset_percentage_ch4(self, value):
        print("Attribute value = ", value)
        self._offsetPercentages[3] = value
        self.info_stream('!!!Writing offset percentage ch4 done!!!')
        offset = value / 100.0
        _thread.start_new_thread(self.changeOffsets, ([4], offset))

    @attribute(dtype=[str],  max_dim_x=4)
    def ChannelsNames(self):
        return self._channelsNames

    @ChannelsNames.setter
    def ChannelsNames(self, value):
        print("Attribute value = ", value)
        self._channelsNames = value
        print(str(self._channelsNames))

    @attribute(dtype=str)
    def TriggerMode(self):
        try:
            return self.AlbaElectr.getTrigmode()
        except Exception as e:
            self.my_logger.error("Exception reading TriggerMode: %s", e)
            self.set_state(DevState.FAULT)

    @TriggerMode.setter
    def TriggerMode(self, value):
        print("Attribute value = ", value)
        try:
            self.AlbaElectr.setTrigmode(value)
            print(value)
        except Exception as e:
            self.my_logger.error("Exception setting trigger mode: %s", e)
            raise

    @attribute(dtype=float)
    def TriggerPeriod(self):
        try:
            period = float(self.AlbaElectr.getTrigperiod())
            period = period / 1000.0
            return period
        except Exception as e:
            self.my_logger.error("Exception reading TriggerPeriod: %s", e)
            self.set_state(DevState.FAULT)

    @TriggerPeriod.setter
    def TriggerPeriod(self, value):
        print("Attribute value = ", value)

        try:
            period = value * 1000.0
            self.AlbaElectr.setTrigperiod(period)
            print(period)
        except Exception as e:
            self.my_logger.error("Exception setting trigger period: %s", e)
            raise

    @attribute(dtype=float)
    def TriggerDelay(self):
        try:
            delay = float(self.AlbaElectr.getTrigDelay())
            delay = delay / 1000.0
            return delay
        except Exception as e:
            self.my_logger.error("Exception reading TriggerDelay: %s", e)
            self.set_state(DevState.FAULT)

    @TriggerDelay.setter
    def TriggerDelay(self, value):
        print("Attribute value = ", value)

        try:
            delay = value * 1000.0
            self.AlbaElectr.setTrigDelay(delay)
            print(delay)
        except Exception as e:
            self.my_logger.error("Exception setting trigger delay: %s", e)
            raise

    @attribute(dtype=int)
    def BufferSize(self):
        try:
            self.__numOfPoints = int(self.AlbaElectr.getPoints())
            return self.__numOfPoints
        except Exception as e:
            self.my_logger.error("Exception reading BufferSize: %s", e)
            self.set_state(DevState.FAULT)

    @BufferSize.setter
    def BufferSize(self, value):
        print("Attribute value = ", value)

        try:
            self.__numOfPoints = value
            self.AlbaElectr.setPoints(self.__numOfPoints)
            print(self.__numOfPoints)
        except Exception as e:
            self.my_logger.error("Exception setting BufferSize: %s", e)
            raise

    @attribute(dtype=float)
    def AvSamples(self):
        try:
            avSamples = float(self.AlbaElectr.getAvsamples())
            avSamples = avSamples / 1000.0
            return avSamples
        except Exception as e:
            self.my_logger.error("Exception reading AvSamples: %s", e)
            self.set_state(DevState.FAULT)

    @AvSamples.setter
    def AvSamples(self, value):
        print("Attribute value = ", value)

        try:
            avSamples = value * 1000.0
            self.AlbaElectr.setAvsamples(avSamples)
            print(avSamples)
        except Exception as e:
            self.my_logger.error("Exception setting AvSamples: %s", e)
            raise

    @attribute(dtype=float)
    def SampleRate(self):
        try:
            sampleRate = int(self.AlbaElectr.getSrate())
            sampleRate = sampleRate / 1000.0
            return sampleRate
        except Exception as e:
            self.my_logger.error("Exception reading SampleRate: %s", e)
            self.set_state(DevState.FAULT)

    @SampleRate.setter
    def SampleRate(self, value):
        print("Attribute value = ", value)

        try:
            sampleRate = value * 1000.0
            self.AlbaElectr.setSrate(sampleRate)
            print(sampleRate)
        except Exception as e:
            self.my_logger.error("Exception setting SampleRate: %s", e)
            raise

    @attribute(dtype=[int], max_dim_x=4096)
    def BufferI1(self):
        try:
            data = self.AlbaElectr.getAvData(1)
            return data
        except Exception as e:
            self.my_logger.error("Exception reading BufferI1: %s", e)
            raise

    @attribute(dtype=float)
    def BufferI1Mean(self):
        try:
            data = self.AlbaElectr.getAvData(1)
            length = len(data)
            mean = sum(data) / length
            return mean
        except Exception as e:
            self.my_logger.error("Exception reading BufferI1Mean: %s", e)
            raise

    @attribute(dtype=[int], max_dim_x=4096)
    def BufferI2(self):
        try:
            data = self.AlbaElectr.getAvData(2)
            return data
        except Exception as e:
            self.my_logger.error("Exception reading BufferI2: %s", e)
            raise

    @attribute(dtype=float)
    def BufferI2Mean(self):
        try:
            data = self.AlbaElectr.getAvData(2)
            length = len(data)
            mean = sum(data) / length
            return mean
        except Exception as e:
            self.my_logger.error("Exception reading BufferI2Mean: %s", e)
            raise

    @attribute(dtype=[int], max_dim_x=4096)
    def BufferI3(self):
        try:
            data = self.AlbaElectr.getAvData(3)
            return data
        except Exception as e:
            self.my_logger.error("Exception reading BufferI3: %s", e)
            raise

    @attribute(dtype=float)
    def BufferI3Mean(self):
        try:
            data = self.AlbaElectr.getAvData(3)
            length = len(data)
            mean = sum(data) / length
            return mean
        except Exception as e:
            self.my_logger.error("Exception reading BufferI3Mean: %s", e)
            raise

    @attribute(dtype=[int], max_dim_x=4096)
    def BufferI4(self):
        try:
            data = self.AlbaElectr.getAvData(4)
            return data
        except Exception as e:
            self.my_logger.error("Exception reading BufferI4: %s", e)
            raise

    @attribute(dtype=float)
    def BufferI4Mean(self):
        try:
            data = self.AlbaElectr.getAvData(4)
            length = len(data)
            mean = sum(data) / length
            return mean
        except Exception as e:
            self.my_logger.error("Exception reading BufferI4Mean: %s", e)
            raise

    @attribute(dtype=str)
    def Firmware_version(self):
        try:
            return self.AlbaElectr.extractSimple(self.AlbaElectr.ask('?FIM'))
        except Exception as e:
            self.my_logger.error("Exception reading Firmware_version: %s", e)
            raise

    @attribute(dtype=str)
    def AlbaEmIP(self):
        try:
            return self.AlbaElectr.extractSimple(self.AlbaElectr.ask('?DEVIP'))

        except Exception as e:
            self.my_logger.error("Exception reading AlbaEmIP: %s", e)
            raise

    @attribute(dtype=str)
    def AlbaEmMAC(self):
        try:
            return self.AlbaElectr.extractSimple(
                self.AlbaElectr.ask('?DEVMAC'))
        except Exception as e:
            self.my_logger.error("Exception reading AlbaEmMAC: %s", e)
            raise

    def checkRanges(self, current, axis):

        dictMinRanges = {'1mA': 1e-6, '100uA': 1e-7, '10uA': 1e-8,
                         '1uA': 1e-9, '100nA': 1e-10, '10nA': 1e-11,
                         '1nA': 1e-12, '100pA': 1e-13}
        dictMaxRanges = {'1mA': 1e-3, '100uA': 1e-4, '10uA': 1e-5,
                         '1uA': 1e-6, '100nA': 1e-7, '10nA': 1e-8,
                         '1nA': 1e-9, '100pA': 1e-10}

        if math.fabs(current) >= dictMaxRanges[self.AllRanges[axis]]:
            return AttrQuality.ATTR_WARNING
        elif math.fabs(current) <= dictMinRanges[self.AllRanges[axis]]:
            return AttrQuality.ATTR_WARNING
        else:
            return AttrQuality.ATTR_VALID

    def convertOffsetToAmp(self, offset, channel):
        """
            Converts the offset in rawdata to amp.
            formula: RawData/10(Voltages(10|-10))*range
            @param offset: offset in rawdata
            @param channel: channel from 1 - 4
        """
        offsetAmp = ((offset / self.AduToVoltConstant) * 10 / 10) * \
            self.dictRanges[self.AllRanges[channel - 1]]
        return offsetAmp

    def readMeasure(self, axis):
        attr = float(self.AlbaElectr.getMeasure(str(axis)))
        return attr

    def readBufferChannel(self, axis):
        attr = self.AlbaElectr.getAvData(axis)
        return attr

    def readBufferMean(self, axis):
        attr = self.AlbaElectr.getAvData(axis)
        length = len(attr)
        mean = sum(attr) / length
        return mean

    def getAllRanges(self):
        rgs = self.AlbaElectr.getRanges(['1', '2', '3', '4'])
        for i, r in enumerate(rgs):
            self.AllRanges[i] = r[1]

    def recoverRanges(self, ranges):
        ranges = [['1', ranges[0]], ['2', ranges[1]],
                  ['3', ranges[2]], ['4', ranges[3]]]
        print("Ranges to write: %s" % ranges)
        self.AlbaElectr.setRanges(ranges)

    @command
    def StopAdc(self):
        self.AlbaElectr.StopAdc()

    @command
    def Stop(self):
        self.AlbaElectr.Stop()

    @command
    def StartAdc(self):
        self.AlbaElectr.StartAdc()

    @command
    def Start(self):
        self.AlbaElectr.Start()

    @command(dtype_in=int)
    def enableChannel(self, axis):
        self.AlbaElectr.enableChannel(axis)

    @command(dtype_in=float)
    def setAvsamples(self, value):
        self.AlbaElectr.setAvsamples(value)

    @command(dtype_in=float)
    def setTrigperiode(self, value):
        self.AlbaElectr.setTrigperiod(value)

    @command(dtype_in=float)
    def setPoints(self, value):
        self.AlbaElectr.setPoints(value)

    @command(dtype_out=str)
    def getEmState(self):
        state = self.AlbaElectr.getState()
        return state

    @command(dtype_in=[str], doc_in="% to correct, channels to correct")
    def offsetCorrection(self, data):
        self.AlbaElectr.stateMoving = True
        percentage = float(data[0])
        channels = eval(data[1])
        dev_proxy = DeviceProxy(self.get_name())
        for i in channels:
            self._offsetPercentages[i - 1] = percentage
            print(f'----------------    offset_percentage_ch{i} {percentage}')
            ch = f'offset_percentage_ch{i}d'
            dev_proxy.write_attribute(ch, percentage)

    @command(dtype_in=str, dtype_out=str)
    def sendCommand(self, cmd):
        answer = self.AlbaElectr.ask(cmd)
        return answer
