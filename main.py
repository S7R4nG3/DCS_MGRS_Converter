# By Icarus747
# Contributors: S7R4nG3
# Created 10/11/2020
import mgrs

class CoordConvert:
    def __init__(self, input_format, input_data):
        self.mgrs = mgrs.MGRS()

        lat, lon = {}, {}
        if input_format.lower() == 'mgrs':
            latd, lond = self.mgrs.toLatLon(input_data)
            lat['d'],lat['m'],lat['s'] = self.mgrs.ddtodms(latd)
            lon['d'],lon['m'],lon['s'] = self.mgrs.ddtodms(lond)
            dms_string = ('N ' if lat['d'] > 0 else 'S ') + '{:.0f} {:.0f} {:.4f}, '.format(lat['d'],lat['m'],lat['s']) + ('E ' if lon['d'] > 0 else 'W ') + '{:.0f} {:.0f} {:.4f}'.format(abs(lon['d']),lon['m'],lon['s'])
            print('\nMGRS to Decimal: {:.4f} {:.4f}'.format(latd,lond))
            print('MGRS to DMS: {}'.format(dms_string))
        if input_format.lower() == 'dd':
            to_mgrs = self.mgrs.toMGRS(input_data[0],input_data[1])
            lat['d'],lat['m'],lat['s'] = self.mgrs.ddtodms(input_data[0])
            lon['d'],lon['m'],lon['s'] = self.mgrs.ddtodms(input_data[1])
            dms_string = 'N {:.0f} {:.0f} {:.4f}, E 0{:.0f} {:.0f} {:.4f}'.format(lat['d'],lat['m'],lat['s'],abs(lon['d']),lon['m'],lon['s'])
            print('\nDecimal to MGRS: {}'.format(to_mgrs))
            print('Decimal to DMS: {}'.format(dms_string))
        if input_format.lower() == 'dms':
            print('\nDMS to Decimal: {}')
            print('DMS to MGRS: {}')


# def main():
#     m = mgrs.MGRS()
#     # dcs = '38TLN046623'
#     dcs = input("Enter MGRS cord.")
#     dd = m.toLatLon(dcs)
#     lat = m.ddtodms(dd[0])
#     Lat = round(lat[1] + lat[2] / 60, 1)
#     long = m.ddtodms(dd[1])
#     Long = round(long[1] + long[2] / 60, 1)
#     print(f"N{int(lat[0])} {Lat}")
#     print(f"E0{int(long[0])} {Long}")

if __name__ == '__main__':
    # main()
    CoordConvert('mgrs', '15TWG0000049776')
    CoordConvert('dd', (42.0, -93.0))
    # CoordConvert('dms', '')