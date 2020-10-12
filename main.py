# By Icarus747
# Contributors: S7R4nG3
# Created 10/11/2020
import mgrs

class CoordConvert:
    def __init__(self, input_format, input_data):
        self.mgrs = mgrs.MGRS()

        lat, lon = {}, {}
        if input_format.lower() == 'mgrs':
            print('\nMGRS Input...', input_data)
            latd, lond = self.mgrs.toLatLon(input_data)
            lat['d'],lat['m'],lat['s'] = self.mgrs.ddtodms(latd)
            lon['d'],lon['m'],lon['s'] = self.mgrs.ddtodms(lond)
            dms_string = ('N ' if lat['d'] > 0 else 'S ') + '{:.0f} {:.0f} {:.4f}, '.format(lat['d'],lat['m'],lat['s']) + ('E ' if lon['d'] > 0 else 'W ') + '{:.0f} {:.0f} {:.4f}'.format(abs(lon['d']),lon['m'],lon['s'])
            print('MGRS to Decimal: {:.6f} {:.6f}'.format(latd,lond))
            print('MGRS to DMS: {}'.format(dms_string))
        if input_format.lower() == 'dd':
            print('\nDecimal Input...', input_data)
            to_mgrs = self.mgrs.toMGRS(input_data[0],input_data[1])
            lat['d'],lat['m'],lat['s'] = self.mgrs.ddtodms(input_data[0])
            lon['d'],lon['m'],lon['s'] = self.mgrs.ddtodms(input_data[1])
            dms_string = ('N ' if lat['d'] > 0 else 'S ') + '{:.0f} {:.0f} {:.4f}, '.format(lat['d'],lat['m'],lat['s']) + ('E ' if lon['d'] > 0 else 'W ') + '{:.0f} {:.0f} {:.4f}'.format(abs(lon['d']),lon['m'],lon['s'])
            print('Decimal to MGRS: {}'.format(to_mgrs))
            print('Decimal to DMS: {}'.format(dms_string))
        if input_format.lower() == 'dms':
            print('\nDMS Input...', input_data)
            lat_float, lon_float = tuple(float(i) for i in input_data[0]), tuple(float(j) for j in input_data[1])
            lat_string = '{:.0f}{:.0f}{:.2f}'.format(lat_float[0],lat_float[1],lat_float[2]) + ( 'N' if lat_float[0] > 0 else 'S' )
            lon_string = '{:.0f}{:.0f}{:.2f}'.format(lon_float[0],lon_float[1],lon_float[2]) + ( 'W' if lon_float[0] > 0 else 'E' )
            lat_to_dd = self.mgrs.dmstodd(lat_string)
            lon_to_dd = self.mgrs.dmstodd(lon_string)
            to_mgrs = self.mgrs.toMGRS(lat_to_dd, lon_to_dd)
            print('DMS to Decimal: {:.6f} {:.6f}'.format(lat_to_dd,lon_to_dd))
            print('DMS to MGRS: {}'.format(to_mgrs))

if __name__ == '__main__':
    CoordConvert('mgrs', '17SNU5478598457')
    CoordConvert('dd', (35.227672, -80.397949))
    CoordConvert('dms', [(35,13,39.6192),(-80,23,52.6516)])