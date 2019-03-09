input2 = '127.0.0.1'
input3 = '.192.168.0.1'
input4 = '10.0.123456.255'
input5 = '172.16'
input6 = '255'
input7 = ''
input8 = '10.10t.10.10'

input1 = input3

segments = 0

if len(input1) == 0:
    print("empty string, no segments")
else:
    length = 0
    for i in range(0,len(input1)):
        if input1[i] in '0123456789':
            length += 1
        elif input1[i] == '.' and length > 0:
            segments += 1
            print("Segment {0} is length {1}".format(segments, length))
            length = 0
            continue
        elif input1[i] == '.':
            continue
        else:
            continue
    if length > 0:
        segments += 1
        print("Segment {0} is length {1}".format(segments, length))