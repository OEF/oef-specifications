OEF file format specifications
==============================

Preambule
---------

All computer strings (i.g. "text") specified in this document are case sensitive
(i.e. if string is lower case, an upper case version is not valid)

Definition
----------
An OEF file is designed to be an ESD data exchange format.
Practically it is an hdf5 file which follow specifications below.

Specifications
--------------
- An open ESD file (oef) is actually an hdf5 file.

- The oef file extension is "oef" (*.oef).

- Oef leaves
  An oef leave is any hdf5 folder containing ESD data

- An oef leave must have

  - an attribute named "oef_data_type" which has is one the string in
    ("tlp", "vfTLP", "hbm", "mm" "hmm") list,
  - and an attribute named "oef_version" which
    is a string following standard strict python conventions for version numbering
    "A version number consists of two or three
    dot-separated numeric components, with an optional "pre-release" tag
    on the end.  The pre-release tag consists of the letter 'a' or 'b'
    followed by a number.  If the numeric components of two version
    numbers are equal, then one with a pre-release tag will always
    be deemed earlier (lesser) than one without."

- An oef leave cannont contain another oef leave.

- The root folder can be an oef leave but then only one measurement can be
  included in the oef file (see point above).

- supported data (in leaves):
 
 - transient waveforms: one leave for current and one leave for voltage

 - if TLP/vfTLP: one leave for I-V curve extracted during measurement

 - functional test/leakage measurement data

- optional: data about the test setup like e.g. tester model, scope model, ...
