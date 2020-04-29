import sys

def validate(results_of_slicing, normalized_sys_argv_2):
    print('normalized_sys_argv_2 = ', normalized_sys_argv_2)
    result = False
    for i in range(len(normalized_sys_argv_2)):
        if i < (len(normalized_sys_argv_2) - 1) and normalized_sys_argv_2[i] == '*':
            results_of_star_search = results_of_slicing.find(normalized_sys_argv_2[i + 1])
            results_of_slicing = results_of_slicing[(results_of_star_search + 1):]

        elif i >= (len(normalized_sys_argv_2) - 1):
            if normalized_sys_argv_2[i] == '*':
                result = True

            elif normalized_sys_argv_2[i] != '*':
                if results_of_slicing[0] == normalized_sys_argv_2[i]:
                    results_of_slicing = results_of_slicing[1:]
                    if results_of_slicing == '':
                        result = True
            break

        elif normalized_sys_argv_2[i] != '*':
            if results_of_slicing[0] != normalized_sys_argv_2[i]:
                break

            elif results_of_slicing[0] == normalized_sys_argv_2[i]:
                results_of_slicing = results_of_slicing[1:]

    return result            


if sys.argv[1] == sys.argv[2]:
    print('OK')

elif '*' not in sys.argv[2] and sys.argv[1] != sys.argv[2]:
    print('KO')

elif '*' in sys.argv[2]:
    # Нормализация данных. Т. к. символ '*' может заменить любой символ в любом количестве, то достаточно привести 
    # повторяющиеся символы '*' к одному подобному символу
    prev = ''
    normalized_sys_argv_2 = ''
    for symbol in sys.argv[2]:
        if symbol == '*':
            prev = '*'
        elif symbol != '*':
            normalized_sys_argv_2 += prev + symbol 
            prev = ''

    if sys.argv[2][-1] == '*':
        normalized_sys_argv_2 += '*'

    if normalized_sys_argv_2 == '*':
        print('OK')   

    else:
        if validate(sys.argv[1], normalized_sys_argv_2):
            print('OK')
        else:
            print('KO')    
        

            

# *.*.*
# **.**.****
# **.**.20**
# __.__.20__

#baaab -> *a*
#baaab -> * | a | *

#baaab -> ***a*
#baaab -> * | a | *

#baaab -> ***a*a*
#baacb -> * | a | * | a | *
#b a 

#acb -> * | a | *
