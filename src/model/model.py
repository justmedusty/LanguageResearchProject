class Model:
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

    def get_ref_date(self):
        return self.ref_date

    def set_ref_date(self, ref_date):
        self.ref_date = ref_date

    def get_gep(self):
        return self.geo

    def set_geo(self, geo):
        self.geo = geo

    def get_dguid(self):
        return self.dguid

    def set_dguid(self, dguid):
        self.dguid = dguid

    def get_area(self):
        return self.area

    def set_area(self, area):
        self.area = area

    def get_uom(self):
        return self.uom

    def set_uom(self, uom):
        self.uom = uom

    def get_uom_id(self):
        return self.uom_id

    def set_uom_id(self, uom_id):
        self.uom_id = uom_id

    def get_scalar_factor(self):
        return self.scalar_factor

    def set_scalar_factor(self, scalar_factor):
        self.scalar_factor = scalar_factor

    def get_scalar_id(self):
        return self.scalar_id

    def set_scalar_id(self, scalar_id):
        self.scalar_id = scalar_id

    def get_vector(self):
        return self.vector

    def set_vector(self, vector):
        self.vector = vector

    def get_coordinate(self):
        return self.coordinate

    def set_coordinate(self, coordinate):
        self.coordinate = coordinate

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def get_status(self):
        return self.status

    def set_status(self, status):
        self.status = status

    def get_symbol(self):
        return self.symbol

    def set_symbol(self, symbol):
        self.scalar_factor = symbol

    def get_terminated(self):
        return self.terminated

    def set_terminated(self, terminated):
        self.terminated = terminated

    def get_decimals(self):
        return self.decimals

    def set_decimals(self, decimals):
        self.decimals = decimals
