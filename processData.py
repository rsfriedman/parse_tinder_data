#!/usr/bin/python

import sys, json

def sum_usage(usage_type, data):
    data_subtype = data[usage_type]
    # print(data_subtype)
    total = 0
    for item in data_subtype:
        total += data_subtype[item]
    return total

def main():
    data_file = str(sys.argv[1])

    with open(data_file, 'r') as f:
        data_dict = json.load(f)

    swipes_right = sum_usage('swipes_likes', data_dict['Usage'])
    print ('Total number of swipes right:', swipes_right)

    swipes_left = sum_usage('swipes_passes', data_dict['Usage'])
    print ('Total number of swipes left:', swipes_left)

    matches = sum_usage('matches', data_dict['Usage'])
    print ('Total number of  matches:', matches)

    messages_exchanged = len(data_dict['Messages'])
    print ('Total number of matches messaged:', messages_exchanged)

    # messages_sent = sum_usage('messages_sent', data_dict['Usage'])
    # print ('Total number of  messages sent:', messages_sent)
    #
    # messages_received = sum_usage('messages_received', data_dict['Usage'])
    # print ('Total number of  messages received:', messages_received)

    # Change to part of your phone number
    phone_number = str(data_dict['Messages']).count('973')
    print('Total times I gave out phone_number: ', phone_number)

if __name__ == '__main__':
    main()
