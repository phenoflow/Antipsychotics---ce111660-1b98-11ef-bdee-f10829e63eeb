# S Jill Stocks, Evangelos Kontopantelis, Artur Akbarov, Sarah Rodgers, Anthony J Avery, Darren M Aschroft, 2024.

import sys, csv, re

codes = [{"code":"2972","system":"gprdproduct"},{"code":"60450","system":"gprdproduct"},{"code":"5014","system":"gprdproduct"},{"code":"40782","system":"gprdproduct"},{"code":"46945","system":"gprdproduct"},{"code":"6064","system":"gprdproduct"},{"code":"59938","system":"gprdproduct"},{"code":"7390","system":"gprdproduct"},{"code":"3197","system":"gprdproduct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('antipsychotics-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["antipsychotics-p13-levomepromazine---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["antipsychotics-p13-levomepromazine---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["antipsychotics-p13-levomepromazine---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
