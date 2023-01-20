from model.model import Model


class CreateRecord:

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

    def create_record(self, ref_date, geo, dguid, area, uom, uom_id, scalar_factor, scalar_id, vector, coordinate,
                      value,
                      status, symbol, terminated, decimals):
        self.new_record = [ref_date, geo, dguid, area, uom, uom_id, scalar_factor, scalar_id, vector, coordinate, value,
                           status, symbol, terminated, decimals]
        return self.new_record
