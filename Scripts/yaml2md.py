import yaml
import io

#TODO: Make better
def generate_packet_markdown(packet):
	table = "Position|Name|Type|Description|SubXor\n"
	table += "--------|----|----|-----------|------\n"

	for i, attr in enumerate(packet['packet']):
		for k in attr:
			if 'subxor' in attr[k]:
				subxor = attr[k]['subxor']
			else:
				subxor = False
			
			if 'description' in attr[k]:
				description = attr[k]['description']
			else:
				description = ""
			
			table += '{0}|{1}|{2}|{3}|{4}\n'.format(i, k, attr[k]['type'], description, subxor)
	return table

if __name__ == "__main__":
	with open("Packets.yml","r") as f: 
		pkts = yaml.load(f)
		
		with open(pkts['header'],"r") as h:
			header = yaml.load(h)
		
		#Generate Table for header
		print(generate_packet_markdown(header))
		
		for p in pkts['packets']:
			#Generate table to index all defined packet types
		
			#Generate tables for each packet type
			with open(p['packet'],"r") as pkt:
				print(generate_packet_markdown(yaml.load(pkt)))
				