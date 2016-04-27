import csv
import sys



def main(input_filename, output_filename):

	with open(input_filename) as infile, open(output_filename,'w') as outfile:

		reader = csv.reader(infile)
		writer = csv.writer(outfile)

		headers = next(reader)
		writer.writerow(headers)

		
		stack = []
		for row in reader:

			product = row[0]
			productType = row[3]

			print(product)
			
			if productType == 'configurable':
				
				for i in stack:
					writer.writerow(i)			

				stack = []
				stack.append(row)


			if not productType:
				stack.append(row)

			if productType == 'simple':
				writer.writerow(row)	


		for i in stack:
			writer.writerow(i)

	

if __name__ == '__main__':
	infile = sys.argv[1]
	outfile = sys.argv[2]
	main(infile,outfile)	


