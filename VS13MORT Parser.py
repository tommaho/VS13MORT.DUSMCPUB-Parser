#
# READ THIS
#   This tools is NOT coded with safety, efficiency, or elegance in mind. Use at your own risk. 
#
# VS13MORT Parser.py
# Author tommaho
# Hosted at https://github.com/tommaho/VS13MORT.DUSMCPUB-Parser
#
# About
#   Converts the 2013 Mortality file located here: http://www.cdc.gov/nchs/data_access/vitalstatsonline.htm
#   to a CSV, based on data file documentation here: http://www.cdc.gov/nchs/data/dvs/Record_Layout_2013.pdf
#
# Directions
#
# 1. Have Python installed.
# 2. Get & unzip mortality file
# 3. Tweak fileObj and FileOutObj to point to the source and destination of your choosing.
#


fileObj = open("C:\data\PO1\VS13MORT.DUSMCPUB",'r')
fileOutObj = open("C:\data\PO1\VS13MORT.csv","a")

fileOutObj.write('Resident_Status, Education, Month_Of_Death, Sex, Age_Key, Age_Value, Age_Sub_Flag, Age_Recode_52, Age_Recode_27, ' + \
                 'Age_Recode_12, Infant_Age_Recode_22, Place_Of_Death, Marital_Status, DOW_of_Death, Data_Year, Injured_At_Work, ' + \
                 'Manner_Of_Death, Method_Of_Disposition, Autopsy, Activity_Code, Place_Of_Causal_Injury,  ICD10, Cause_Recode_358, ' + \
                 'Cause_Recode_113, Infant_Cause_Recode_130, Cause_Recode_39, Entity_Axis_Conditions, EAC1, EAC2, EAC3, EAC4, EAC5, ' + \
                 'EAC6, EAC7, EAC8, EAC9, EAC10, EAC11, EAC12, EAC13, EAC14, EAC15, EAC16, EAC17, EAC18, EAC19, EAC20, ' + \
                 'Record_Axis_Conditions, RA1, RA2, RA3, RA4, RA5, RA6, RA7, RA8, RA9, RA10, RA11, RA12, RA13, RA14, ' + \
                 'RA15, RA16, RA17, RA18, RA19, RA20, Race, Race_Bridged, Race_Imputation, Race_Recode_3, Race_Recode_5, ' + \
                 'Hispanic_Origin, Hispanic_Origin_Recode\n')

outStr = ""

for line in fileObj:

               Resident_Status = line[19].strip()
               Education = line[60:62].strip()
               Month_Of_Death = line[63:67].strip()
               Sex = line[68].strip()
               Age_Key = line[69].strip()
               Age_Value = line[70:73].strip()
               Age_Sub_Flag = line[73].strip()
               Age_Recode_52 = line[74:76].strip()
               Age_Recode_27 = line[76:78].strip()
               Age_Recode_12 = line[78:80].strip()
               Infant_Age_Recode_22 = line[80:82].strip()
               Place_Of_Death = line[82].strip()
               Marital_Status = line[83].strip()
               DOW_of_Death = line[84].strip()
               Data_Year = line[101:105].strip()
               Injured_At_Work = line[105].strip()
               Manner_Of_Death = line[106].strip()
               Method_Of_Disposition = line[107].strip()
               Autopsy = line[108].strip()
               Activity_Code = line[143].strip()
               Place_Of_Causal_Injury = line[144].strip()
               ICD10 = line[145:149].strip()
               Cause_Recode_358 = line[149:152].strip()
               Cause_Recode_113 = line[153:156].strip()
               Infant_Cause_Recode_130 = line[156:159].strip()
               Cause_Recode_39 = line[159:161].strip()
               Entity_Axis_Conditions = line[162:164].strip()
               EAC1 = line[164:171].strip()
               EAC2 = line[171:178].strip()
               EAC3 = line[178:185].strip()
               EAC4 = line[185:192].strip()
               EAC5 = line[192:199].strip()
               EAC6 = line[199:206].strip()
               EAC7 = line[206:213].strip()
               EAC8 = line[213:220].strip()
               EAC9 = line[220:227].strip()
               EAC10 = line[227:234].strip()
               EAC11 = line[234:241].strip()
               EAC12 = line[241:248].strip()
               EAC13 = line[248:255].strip()
               EAC14 = line[255:262].strip()
               EAC15 = line[262:269].strip()
               EAC16 = line[269:276].strip()
               EAC17 = line[276:283].strip()
               EAC18 = line[283:290].strip()
               EAC19 = line[290:297].strip()
               EAC20 = line[297:304].strip()
               Record_Axis_Conditions = line[340:342]
               RA1 = line[343:348].strip()
               RA2 = line[348:353].strip()
               RA3 = line[353:358].strip()
               RA4 = line[358:363].strip()
               RA5 = line[363:368].strip()
               RA6 = line[368:373].strip()
               RA7 = line[373:378].strip()
               RA8 = line[378:383].strip()
               RA9 = line[383:388].strip()
               RA10 = line[388:393].strip()
               RA11 = line[393:398].strip()
               RA12 = line[398:403].strip()
               RA13 = line[403:408].strip()
               RA14 = line[408:413].strip()
               RA15 = line[413:418].strip()
               RA16 = line[418:423].strip()
               RA17 = line[423:428].strip()
               RA18 = line[428:433].strip()
               RA19 = line[433:438].strip()
               RA20 = line[438:443].strip()
               Race = line[444:446].strip()
               Race_Bridged = line[446].strip()
               Race_Imputation = line[447].strip()
               Race_Recode_3 = line[448].strip()
               Race_Recode_5 = line[449].strip()
               Hispanic_Origin = line[483:486].strip()
               Hispanic_Origin_Recode = line[487].strip()
               
               
               
               
               
               outStr = (Resident_Status +              ', ' + Education +              ', ' + Month_Of_Death +         ', ' + Sex + \
                         ', ' + Age_Key +               ', ' + Age_Value +              ', ' + Age_Sub_Flag +           ', ' + Age_Recode_52 + \
                         ', ' + Age_Recode_27 +         ', ' + Age_Recode_12 +          ', ' + Infant_Age_Recode_22 +   ', ' + Place_Of_Death + \
                         ', ' + Marital_Status +        ', ' + DOW_of_Death +           ', ' + Data_Year +              ', ' + Injured_At_Work +  \
                         ', ' + Manner_Of_Death +       ', ' + Method_Of_Disposition +  ', ' + Autopsy +                ', ' + Activity_Code + \
                         ', ' + Place_Of_Causal_Injury +', ' + ICD10 +                  ', ' + Cause_Recode_358 +       ', ' + Cause_Recode_113 +  \
                         ', ' + Infant_Cause_Recode_130 + ', ' + Cause_Recode_39 +      ', ' + Entity_Axis_Conditions + ', ' + EAC1 + \
                         ', ' + EAC2 +                  ', ' + EAC3 +                   ', ' + EAC4 +                   ', ' + EAC5 + \
                         ', ' + EAC6 +                  ', ' + EAC7 +                   ', ' + EAC8 +                   ', ' + EAC9 + \
                         ', ' + EAC10 +                 ', ' + EAC11 +                  ', ' + EAC12 +                  ', ' + EAC13 + \
                         ', ' + EAC14 +                 ', ' + EAC15 +                  ', ' + EAC16 +                  ', ' + EAC17 + \
                         ', ' + EAC18 +                 ', ' + EAC19 +                  ', ' + EAC20 +                  ', ' + Record_Axis_Conditions + \
                         ', ' + RA1 +                   ', ' + RA2 +                    ', ' + RA3 +                    ', ' + RA4 + \
                         ', ' + RA5 +                   ', ' + RA6 +                    ', ' + RA7 +                    ', ' + RA8 + \
                         ', ' + RA9 +                   ', ' + RA10 +                   ', ' + RA11 +                   ', ' + RA12 + \
                         ', ' + RA13 +                  ', ' + RA14 +                   ', ' + RA15 +                   ', ' + RA16 + \
                         ', ' + RA17 +                  ', ' + RA18 +                   ', ' + RA19 +                   ', ' + RA20 + \
                         ', ' + Race +                  ', ' + Race_Bridged +           ', ' + Race_Imputation +        ', ' + Race_Recode_3 + \
                         ', ' + Race_Recode_5 +         ', ' + Hispanic_Origin +        ', ' + Hispanic_Origin_Recode + '\n')


               
               fileOutObj.write(outStr)



print("Parse complete.")
fileOutObj.close()
fileObj.close()

