#Dict

#syntax : {Key:Value}
#heterogenous
#ordered
#indexed (not numeric) key works a s index
#Key duplicates are allowed but old gets overwritten


data={"Name":"Let us C", "Author":" Y Kanetkar","Price":340,"Publication":"BPB Publication","Name":"Let us C++"}#key value pair 4

print("Data type: ",type(data))
print("Length of data: ",len(data))
print(data)

print(data["Author"])