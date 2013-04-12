# -*- coding: utf-8 -*-
import os
from distutils.version import StrictVersion
import h5py

oef_data_type = ("tlp", "hbm", "mm")
oef_versions = ("0.1a1",)
oef_required_attributes = {'oef_data_type', 'oef_version'}

debug = True


class OefLeaveList(list):

    def __init__(self):
        list.__init__(self)

    def add_from(self, oef_file):
        oef_file.visititems(self.add_if_valid)

    def add_if_valid(self, name, item):
        print "In", name
        if type(item) is h5py.Group:
            attrs = item.attrs
            if oef_required_attributes.issubset(attrs.keys()):
                try:
                    StrictVersion(attrs['oef_version'])
                except ValueError:
                    print 'Skiping, invalid oef_version "%s":' % attrs['oef_version']
                    print "-" * 20
                    return
                if (attrs['oef_data_type'] in oef_data_type
                        and attrs['oef_version'] in oef_versions):
                    self.append(item)
                    if debug:
                        print "Added"
                elif debug:
                    print "Skiping",
                    if attrs['oef_data_type'] not in oef_data_type:
                        print 'does not have a valid oef_data_type: "%s"' % attrs['oef_data_type']
                    if attrs['oef_version'] not in oef_versions:
                        print 'does not have a known oef version number: "%s"' % attrs['oef_version']
            else:
                missing = oef_required_attributes - set(attrs.keys())
                print "Skiping, does not have required attribute(s):", missing
        print "-" * 20


def scan_oef(oef_file_name):
    if not os.path.isfile(oef_file_name):
        print "This is not a file"
        return False
    if not os.path.splitext(oef_file_name)[1] == ".oef":
        print "The file does not have an oef extension"
        return False
    if not h5py.is_hdf5(oef_file_name):
        print "This is not an hdf5 file"
        return False
    valid_oef_leave_list = OefLeaveList()
    with h5py.File(oef_file_name, 'r') as oef_file:
        valid_oef_leave_list.add_from(oef_file)
        if len(valid_oef_leave_list) == 0:
            print "No valid leave found"
            return False
        else:
            for elem in valid_oef_leave_list:
                if elem.parent in valid_oef_leave_list:
                    print "Something wrong !", elem.name, "is in", elem.parent.name,
                    print "which is itself a valid oef leaf"
    return True

if __name__ == '__main__':
    scan_oef('demo.oef')
