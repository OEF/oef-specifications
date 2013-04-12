# -*- coding: utf-8 -*-
import h5py

oef_file = h5py.File('demo.oef', 'w')

grp = oef_file.create_group('experiment1')

grp = oef_file.create_group('experiment2')
grp.attrs['oef_data_type'] = 'tlp'

grp = oef_file.create_group('experiment3')
grp.attrs['oef_data_type'] = 'tlp'
grp.attrs['oef_version'] = '0.1dev'

grp = oef_file.create_group('experiment4')
grp.attrs['oef_data_type'] = 'tlb'
grp.attrs['oef_version'] = '0.1a1'

grp = oef_file.create_group('experiment5')
grp.attrs['oef_data_type'] = 'tlp'
grp.attrs['oef_version'] = '0.1a2'

grp = oef_file.create_group('experiment6')
grp.attrs['oef_data_type'] = 'tlp'
grp.attrs['oef_version'] = '0.1a1'

grp = oef_file.create_group('experiment6/experiment7')
grp.attrs['oef_data_type'] = 'tlp'
grp.attrs['oef_version'] = '0.1a1'

oef_file.flush()
oef_file.close()
