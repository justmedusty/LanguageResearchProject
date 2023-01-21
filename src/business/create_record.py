class CreateRecord:
    """
        The function takes in a list of values and assigns them to the attributes of the class

        :param ref_date: The reference date for the data value
        :param geo: The geographic code for the area
        :param dguid: The Dimensional GUID is a unique identifier for each data point
        :param area: The area of the data
        :param uom: unit of measure
        :param uom_id: The unit of measure identifier
        :param scalar_factor: The scalar factor is a number that is used to multiply the value of the data
        :param scalar_id:
        :param vector: A two-character code that indicates the vector of the data
        :param coordinate: The coordinate of the data point
        :param value: The value of the observation
        :param status:
        :param symbol: The symbol of the data series
        :param terminated:
        :param decimals: The number of decimal places to which the value is rounded
        """

    def __init__(self, ref_date, geo, dguid, area, uom, uom_id, scalar_factor, scalar_id, vector, coordinate, value,

                 status, symbol, terminated, decimals):
        self.ref_date = ref_date
        self.geo = geo
        self.dguid = dguid
        self.area = area
        self.uom = uom
        self.uom_id = uom_id
        self.scalar_factor = scalar_factor
        self.scalar_id = scalar_id
        self.vector = vector
        self.coordinate = coordinate
        self.value = value
        self.status = status
        self.symbol = symbol
        self.terminated = terminated
        self.decimals = decimals

        self.new_record = []

    """
        This function takes in 15 arguments and returns a list of those 15 arguments
        
        :param ref_date: The reference date of the data
        :param geo: The geographic code for the area
        :param dguid: the unique identifier for the data
        :param area: The area of the data
        :param uom: unit of measure
        :param uom_id: unit of measure identifier
        :param scalar_factor: The scalar factor is a number that is used to multiply the value of the data element
        :param scalar_id: 1
        :param vector: A string that represents the vector of the data
        :param coordinate: 
        :param value: the value of the data
        :param status: 
        :param symbol: The symbol is a unique identifier for the data value. It is a combination of the DIMENSION_ID and the
        DIMENSION_MEMBERS
        :param terminated: 
        :param decimals: number of decimal places
        :return: The new_record is being returned.
        """

    def create_record(self, ref_date, geo, dguid, area, uom, uom_id, scalar_factor, scalar_id, vector, coordinate,

                      value,
                      status, symbol, terminated, decimals):
        self.new_record = [ref_date, geo, dguid, area, uom, uom_id, scalar_factor, scalar_id, vector, coordinate, value,
                           status, symbol, terminated, decimals]
        return self.new_record
