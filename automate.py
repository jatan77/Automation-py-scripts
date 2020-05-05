import sys 
import os
import subprocess as sp

def bom():
                    """
                    old testing code
                    
                    with open("clendom.txt") as f:
                        with open("dom1.txt", "w") as f1:
                            for line in f:
                                f1.write(line)
                    with open("clendom.txt") as f:
                        with open("dom2.txt", "w") as f1:
                            for line in f:
                                f1.write(line)            
                               
                    file_name = "dom1.txt"
                    with open(file_name, 'r') as f:
                        file_lines = ['http://'+''.join([x.strip(),'/', '\n']) for x in f.readlines()]
                    with open(file_name, 'w') as f:
                        f.writelines(file_lines) 

                    file_name = "dom2.txt"
                    with open(file_name, 'r') as f:
                        file_lines = ['https://'+''.join([x.strip(),'/', '\n']) for x in f.readlines()]
                    with open(file_name, 'w') as f:
                        f.writelines(file_lines) 

                    filenames = ['dom1.txt', 'dom2.txt'] 
                    with open('alldomof.txt', 'w') as outfile: 
                        for names in filenames: 
                            with open(names) as infile: 
                                outfile.write(infile.read()) 
                            outfile.write("\n")  
                    with open('alldomof.txt') as infile, open('alldom.txt', 'w') as outfile:
                        for line in infile:
                            if not line.strip(): continue
                            outfile.write(line)
                                  
                    os.remove("dom1.txt")
                    os.remove("dom2.txt")
                    os.remove("alldomof.txt")
                    os.system("cp alldom.txt /home/username/tool/webscreenshot-2.9/webscreenshot")
                    os.system("cp alldom.txt /home/username/tool/open-redirect-scanner-master")                  
                    os.remove("alldom.txt")
                    """
                    
                    
                    os.chdir('/home/username/tool/webscreenshot-2.9/webscreenshot') 
                    cod1 = "python webscreenshot.py -i "+fil+" -o "+ commandstring + " -w 10 -m"
                    print("[*]Running :"+cod1);
                    sp.Popen('gnome-terminal -e "'+cod1+'"', shell=True)
                    
commandstring = '';  

for arg in sys.argv[1:]: 
    if ' ' in arg:
        commandstring+= '"{}"  '.format(arg) ;  
    else:
        commandstring+="{}  ".format(arg) ;     


command = "python sublist3r.py -d "+ commandstring + "-o maindom.txt"
print("\n[*]Running : "+command); 

g = raw_input("\n[*] Do you want to take Screen short of all subdomains? y/n : ") 
os.system(command)  

print("\n[*]Cleaning domains : "); 

a_string = commandstring
split_string = a_string.split(".", 1)
c = split_string[0]
b=c.replace(" ","")
fil="clean-"+b+".txt"

with open("maindom.txt") as f:
    with open(fil, "w") as f1:
        for line in f:
            rep=line.replace('<BR>', '\n')
            f1.write(rep)
print("[*]Saving into : "+fil);             
os.remove("maindom.txt")     
os.system("cp "+fil+" /home/username/tool/webscreenshot-2.9/webscreenshot") 
print("[*]Sending "+fil+" to: Webscreenshot\n");  
if g == "y":
   bom()
else:
   print("Every thing is DONE")

