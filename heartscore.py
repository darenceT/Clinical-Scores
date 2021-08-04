import klembord
klembord.init()

heart_score_guide = """
 1. Suspicious History:         slightly [0]    moderately [1]          highly [2]
 2. EKG:                        normal [0]      nonspecific repol [1]   ST changes [2]
 3. Age:                        < 45 [0]        45-64 [1]               >= 65 [2]
 4. RF:                         none[0]         1-2 [1]                 >= 3 [2]                          
    (htn,hl,fat,cig,fh,athero)
 5. Troponin:                   < normal [0]    1-3x normal [1]         > 3x normal [2]"""

prompt_user = '    Enter score (e.g. 01210): '
prompt_user2 = '    Enter score again (e.g. 11120, only 5 numbers): '

print(heart_score_guide)
enter_score = input(prompt_user)

while not len(enter_score) == 5:
    print(heart_score_guide)
    enter_score = input(prompt_user2)



values_list = [int(i) for i in str(enter_score)]
final_score = sum(values_list)

def display_score():
    print()
    print('     HEART Score for Major Cardiac Events')
    print('1. Suspicious history:', values_list[0])
    print('2. EK:', values_list[1])
    print('3. Age:', values_list[2])
    print('4. RF:', values_list[3])
    print('5. Troponin:', values_list[4])
    print()

display_score()
print('HEART SCORE:', final_score)
print(""" 
Backus et al externally validated the HEART Score with a prospective multicenter study 
in 2013. The study evaluated 2,440 patients presenting with chest pain to 10 emergency
departments in the Netherlands. The primary endpoint was the occurrence of any MACE 
within 6 weeks. The performance of the HEART Score was also compared to that of the 
TIMI Score for UA/NSTEMI and the GRACE ACS Risk Score. In the low risk group (score 
0-3), 15/870 (1.7%) of patients were found to have a MACE. In patients with HEART 
scores 4-6, MACE was diagnosed in 183/1101 (16.6%). In patients with high HEART scores 
(values 7-10), MACE occurred in 50.1%. The c-statistic of the HEART score (0.83) was 
significantly higher than the c-statistic of TIMI (0.75) and GRACE (0.70) respectively 
(p <0.0001).""")


klembord.set_with_rich_text('', """
                            hello testing, <strong>itallic words here</strong>""")

print('**********The above text has been copied to your clipboard*************')