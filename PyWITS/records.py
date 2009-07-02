#all WITS records defined as python dictionaries!
#look at record 0101 for the template!
#some records may be incomplete
#2008 Kenneth Miller
general_time_based = {'01':{'description':'Well Identifier',
                            'long_mnemonic':'WELLID',
                            'short_mnemonic':'WID',
                            'type':'A',
                            'length':16,
                            'metric_units':None,
                            'fps_units':None
                            },
                      
                      '08':{'description':'Bit Depth (meas)'},
                      '10':{'description':'Depth Hole (meas)'},
                      '12':{'description':'Block Position'},
                      '13':{'description':'Rate of Penetration (avg)'},
                      '15':{'description':'Hookload (max)'},
                      '17':{'description':'Weight on Bit (surf,max)'},
                      '19':{'description':'Rotary Torque (surf,max)'},
                      '20':{'description':'Rotary Speed (surf,avg)'},
                      '21':{'description':'Standpipe Pressure (avg)'},
                      '23':{'description':'Pump Stroke Rate #1'},
                      '24':{'description':'Pump Stroke Rate #2'},
                      '25':{'description':'Pump Stroke Rate #3'},
                      '26':{'description':'Tank Volume (active)'},
                      '28':{'description':'Mud Flow Out (%)'},
                      '30':{'description':'Mud Flow In (avg)'},
                      '37':{'description':'Pump Stroke Count (cum)'},
                      '39':{'description':'Depth Returns (meas)'},
                      '40':{'description':'Gas (avg)'},
                      }
                      
configuration = {'84':{'description':'Vendor 1 Name/Service'}}

all = {'01':general_time_based,
       '18':configuration}

if __name__ == '__main__':
    print all
