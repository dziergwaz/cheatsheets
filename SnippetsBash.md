# BASH CHEATS SHEETS


## 01_05 Bash expansions and substitutions
```bash
echo ~
echo ~-
```

## 01_06 Brace expansion
```bash
echo {1..10}
echo {10..1}
echo {01..10}
echo {01..100}
{echo a..z}
echo {Z..A}
echo {1..30..3}
echo {a..z..2}
touch file_{01..12}{a..d}
echo {cat,dog,fox}
echo {cat,dog,fox}_{1..5}
```

## 01_07 Parameter expansion
```bash
greeting="hello there!"
echo $greeting
echo ${greeting:6}
echo ${greeting:6:3}
echo ${greeting/there/everybody}
echo ${greeting//e/_}
echo ${greeting/e/_}
echo $greeting:4:3
```

## 01_08 Command substitution
```bash
uname -r
echo "The kernel is $(uname -r)."
echo "Result: $(python3 -c 'print("Hello from Python!")' | tr [a-z] [A-Z])"
```

## 01_09 Arithmetic expansion
```bash
echo $(( 2 + 2 ))
echo $(( 4 - 2 ))
echo $(( 4 * 5 ))
echo $(( 4 / 5 ))
```

## 02_01 Understanding Bash script syntax
```bash
nano myscript

#!/usr/bin/env bash
echo "hello"

# This is a comment
echo "there"

chmod +x myscript
./myscript
```

## 02_03 Displaying text with 'echo'
```bash
echo hello world
worldsize=big
echo hello $worldsize world
echo "The kernel is $(uname -r)"
echo The kernel is $(uname -r)
echo The (kernel) is $(uname -r)
echo The \(kernel\) is $(uname -r)
echo 'The kernel is $(uname -r)'
echo "The (kernel) is $(uname -r)"
echo "The (kernel) is \$(uname -r)"
echo
echo; echo "More space!"; echo
echo -n "No newline"
echo -n "Part of "; echo -n "a statement"
```

## 02_04 Working with variables

```bash
#!/usr/bin/env bash

mygreeting=hello
mygreeting2="Good Morning"
number=6

echo $mygreeting
echo $mygreeting2
echo $number
```

```bash
#!/usr/bin/env bash

myvar="Hello!"
echo "The value of the myvar variable is: $myvar"
myvar="Bonjour!"
echo "The value of the myvar variable is: $myvar"

declare -r myname="Scott"
echo "The value of the myname variable is: $myname"
myname="Michael"
echo "The value of the myname variable is: $myname"

declare -l lowerstring="This is some TEXT!"
echo "The value of the lowerstring variable is: $lowerstring"
lowerstring="Let's CHANGE the VALUE!"
echo "The value of the lowerstring variable is: $lowerstring"

declare -u upperstring="This is some TEXT!"
echo "The value of the upperstring variable is: $upperstring"
upperstring="Let's CHANGE the VALUE!"
echo "The value of the upperstring variable is: $upperstring"
```

```bash
declare -p
env
echo $USER
```

## 02_05 Working with numbers
```bash
echo $((4+4))
echo $((8-5))
echo $((2*3))
echo $((8/4))
echo $(( (3+6) - 5 * (5-2) ))
a=3
((a+=3))
echo $a
((a++))
echo $a
((a++))
echo $a
((a--))
echo $a
(($a++))
((a++))
echo $a
a=$a+2
echo $a
declare -i b=3
b=$b+3
echo $b
echo $((1/3))
declare -i c=1
declare -i d=3
e=$(echo "scale=3; $c/$d | bc)
echo $e
echo $RANDOM
echo $(( 1 + $RANDOM % 10 ))
echo $(( 1 + $RANDOM % 20 ))
```

## 02_06 Comparing values with test
```bash
help test
[ -d ~ ]
echo $?
[ -d /bin/bash ]; echo $?
[ -d /bin ]; echo $?
[ "cat" = "dog" ]; echo $?
[ "cat" = "cat" ]; echo $?
[ 4 -lt 5 ]; echo $?
[ 4 -lt 3 ]; echo $?
[ ! 4 -lt 3 ]; echo $?
```

## 02_07 Comparing values with extended test
```bash
[[ 4 -lt 3 ]]; echo $?
[[ -d ~ && -a /bin/bash ]]; echo $?
[[ -d ~ && -a /bin/mash ]]; echo $?
[[ -d ~ || -a /bin/bash ]]; echo $?
[[ -d /bin/bash ]] && echo ~ is a directory
ls && echo "listed the directory"
true && echo "success!"
false && echo "success!"
[[ "cat" =~ c.* ]]; echo $?
[[ "bat" =~ c.* ]]; echo $?
```

## 02_08 Formatting and styling text output
```bash
echo -e "Name\t\tNumber"; echo -e "Scott\t\t123"
echo -e "This text\nbreaks over\nthree lines"
echo -e "\a"
echo -e "Ding\a"
```

```bash
#!/usr/bin/env bash
echo -e "\033[33;44mColor Text\033[0m"
echo -e "\033[30;42mColor Text\033[0m"
echo -e "\033[41;105mColor Text"
echo "some text that shouldn't have styling"
echo -e "\033[0m"
echo "some text that shouldn't have styling"
echo -e "\033[4;31;40mERROR:\033[0m\033[31;40m Something went wrong.\033[0m"
```

```bash
#!/usr/bin/env bash

ulinered="\033[4;31;40m"
red="\033[31;40m"
none="\033[0m"

echo -e $ulinered"ERROR:"$none$red" Something went wrong."$none
```

## 02_09 Formatting output with printf
```bash
echo "The results are: $(( 2 + 2 )) and $(( 3 / 1 ))"
printf "The results are: %d and %d\n" $(( 2 + 2 )) $(( 3 / 1 ))
```

```bash
#!/usr/bin/env bash

echo "----10----| --5--"

echo "Right-aligned text and digits"
printf "%10s: %5d\n" "A Label" 123 "B Label" 456

echo "Left-aligned text, right-aligned digits"
printf "%-10s: %5d\n" "A Label" 123 "B Label" 456

echo "Left-aligned text and digits"
printf "%-10s: %-5d\n" "A Label" 123 "B Label" 456

echo "Left-aligned text, right-aligned and padded digits"
printf "%-10s: %05d\n" "A Label" 123 "B Label" 456

printf "%10s %5d\n" "abcd" 123
printf "%-10s %-5d\n" "abcd" 123
printf "%10s %-5d\n" "abcd" 123

echo "----10----| --5--"
```

```bash
printf "%(%Y-%m-%d %H:%M:%S)T\n" 1658179558
date +%s
date +%Y-%m-%d\ %H:%M:%S
printf "%(%Y-%m-%d %H:%M:%S)T\n" $(date +%s)
printf "%(%Y-%m-%d %H:%M:%S)T\n"
printf "%(%Y-%m-%d %H:%M:%S)T is %s\n" -1 "the time"
```

## 02_10 Working with arrays
```bash
declare -a snacks=("apple" "banana" "orange")
echo ${snacks[2]}
snacks[5]="grapes"
snacks+=("mango")
echo ${snacks[@]}
for i in {0..6}; do echo "$i: ${snacks[$i]}"; done
declare -A office
office[city]="San Francisco"
office["building name"]="HQ West"
echo "${office["building name"]} is in ${office[city]}"
```

## 03_01 Conditional statements with the 'if' keyword

```bash
#!/usr/bin/env bash

declare -i a=3

if [[ $a -gt 4 ]]; then
    echo "$a is greater than 4!"
else
    echo "$a is not greater than 4!"
fi
```

```bash
#!/usr/bin/env bash

declare -i a=3

if [[ $a -gt 4 ]]; then
    echo "$a is greater than 4!"
elif (( $a > 2 )); then
    echo "$a is greater than 2."
else
    echo "$a is not greater than 4!"
fi
```

## 03_02 Working with while and until loops
```bash
#!/usr/bin/env bash

echo "While Loop"

declare -i n=0
while (( n < 10 ))
do
    echo "n:$n"
    (( n++ ))
done

echo -e "\nUntil Loop"
declare -i m=0
until (( m == 10 )); do
    echo "m:$m"
    (( m++ ))
done
```

```bash
#!/usr/bin/env bash

echo "While Loop"

declare -i n=0
while (( n < 10 ))
do
    echo "n:$n"
    (( n++ ))
done

echo -e "\nUntil Loop"
declare -i m=0
until ((m > m)); do
    echo "m:$m"
    (( m++ ))
done
```

## 03_03 Introducing 'for' loops
```bash
#!/usr/bin/env bash

for i in 1 2 3
do
    echo $i
done

for i in 1 2 3; do echo $i; done
```

```bash
#!/usr/bin/env bash

for i in {1..100}
do
    echo $i
done
```

```bash
#!/usr/bin/env bash

for (( i=1; i<=100; i++ ))
do
    echo $i
done
```

```bash
#!/usr/bin/env bash

declare -a fruits=("apple" "banana" "cherry")
for i in ${fruits[@]}
do
    echo $i
done
```

```bash
#!/usr/bin/env bash

declare -A arr
arr["name"]="scott"
arr["id"]="1234"
for i in "${!arr[@]}"
do
    echo $i: "${arr[$i]}"
done
```

```bash
#!/usr/bin/env bash

for i in $(ls)
do
    echo "Found a file: $i"
done
```

```bash
#!/usr/bin/env bash

for i in *
do
    echo "Found a file: $i"
done
```

## 03_04 Selecting behavior using 'case'
```bash
#!/usr/bin/env bash
animal="dog"
case $animal in
    bird) echo "Avian";;
    dog|puppy) echo "Canine";;
    *) echo "No match!"
esac
done 

```

```bash
# CASE WYBOR
select animal in "wybor 1" "wybor 2" "wybor 3" "wybor 4"
do
case $animal in
    "wybor 1") echo "1111";;
    "wybor 2"|"wybor 3") echo "2222";;
    *) echo "default" ; exit ;;
esac
done
```

## 03_05 Using functions
```bash
#!/usr/bin/env bash

greet() {
    echo "Hi there."
}

echo "And now, a greeting..."
greet
```

```bash
#!/usr/bin/env bash

greet() {
    echo "Hi there, $1"
}

echo "And now, a greeting..."
greet Scott
```

```bash
#!/usr/bin/env bash

greet() {
    echo "Hi there, $1. What a nice $2"
}

echo "And now, a greeting..."
greet Scott Morning
greet Everybody Evening
```

```bash
#!/usr/bin/env bash

numberthing() {
    declare -i i=1
    for f in $@; do
        echo "$i: $f"
        (( i += 1 ))
    done
    echo "This counting was brought to you by $FUNCNAME."
}

numberthing "$(ls /)"
echo
numberthing pine birch maple spruce
```

```bash
#!/usr/bin/env bash

var1="I'm variable 1"

myfunction() {
    var2="I'm variable 2"
    local var3="I'm variable 3"
}
myfunction

echo $var1
echo $var2
echo $var3
```

## 03_06 Reading and writing text files
```bash
#!/usr/bin/env bash

for i in 1 2 3 4 5
do
    echo "This is line $i" > ~/textfile.txt
done
```

```bash
#!/usr/bin/env bash

for i in 1 2 3 4 5
do
    echo "This is line $i" >> ~/textfile.txt
done
```

```bash
#!/usr/bin/env bash

while read f
    do echo "I read a line an it says: $f"
done < ~/textfile.txt
```

## 04_01 Working with arguments
```bash
#!/usr/bin/env bash

echo "The $0 script got the argument $1"
```

```bash
#!/usr/bin/env bash

echo "The $0 script got the argument $1"
echo "Argument 2 is $2"
```

```bash
#!/usr/bin/env bash

for i in $@
do
    echo $i
done
```

```bash
#!/usr/bin/env bash

for i in $@
do
    echo $i
done

echo "There were $# arguments."
#print arguments that were given
#./script arg1 "arg2 arg3" ...
#after : arg1\narg2arg3\n...
```

## 04_02 Working with options
```bash
#!/usr/bin/env bash

while getopts u:p: option; do
    case $option in
        u) user=$OPTARG;;
        p) pass=$OPTARG;;
    esac
done

echo "user: $user / pass: $pass"

# terminal : ./myscript  -b asd -a akmd
# putput: aaa akmd \n bbb asd
```

```bash
#!/usr/bin/env bash

while getopts u:p:ab option; do
    case $option in
        u) user=$OPTARG;;
        p) pass=$OPTARG;;
        a) echo "got the A flag";;
        b) echo "got the B flag";;
    esac
done

echo "user: $user / pass: $pass"
```

```bash
#!/usr/bin/env bash

while getopts :u:p:ab option; do
    case $option in
        u) user=$OPTARG;;
        p) pass=$OPTARG;;
        a) echo "got the A flag";;
        b) echo "got the B flag";;
        ?) echo "I don't know what $OPTARG is!"
    esac
done

echo "user: $user / pass: $pass"
```

## 04_03 Getting input during execution
```bash
#!/usr/bin/env bash

echo "What is your name?"
read name
echo "What is your password?"
read -s pass
read -p "What's your favorite animal? " animal

echo "name: $name, pass: $pass, animal: $animal"
```
```bash
help read
```

```bash
#!/usr/bin/env bash

echo "Which animal"
select animal in "bird" "dog" "bird" "fish"
do
    echo "You selected $animal!"
    break
done
```

```bash
#!/usr/bin/env bash

echo "Which animal"
select animal in "bird" "dog" "quit"
do
    case $animal in
        bird) echo "Birds like to fly.":;
        dog) echo "Dogs like to play catch.";;
        quit) break;;
        *) echo "I'm not sure what that is.";;
done
```

## 04_04 Ensuring a response
```bash
#!/usr/bin/env bash

read -ep "Favorite color? " -i "Blue" favcolor
echo $favcolor
```

```bash
#!/usr/bin/env bash

if (($#<3)); then
    echo "This command requires three arguments:"
    echo "username, userid, and favorite number."
else
    # the program goes here
    echo "username: $1"
    echo "userid: $2"
    echo "favorite number: $3"
fi
```

```bash
#!/usr/bin/env bash

read -p "Favorite animal? " fav
while [[ -z $fav ]]
do
        read -p "I need an answer! " fav
done

echo "$fav was selected."
```

```bash
#!/usr/bin/env bash

read -p "Favorite animal? [cat] " fav
if [[ -z $fav ]]; then
        fav="cat"
fi
echo "$fav was selected"
```

```bash
#!/usr/bin/env bash

read -p "year : " year
#re='^[[:digit:]]{4}$'

while [[ ! $year =~ ^[0-9]{4}$ ]]; do
    
    read -p "it's not that hard : " year
    
done
echo "selected year ${year}"
```
# BRACE EXPANSION

1. 
a. create folder Data, in that folder create files for each day, each month from 2010 - 2019
create folder Backup, inside that folder create more in accordance with pattern dYYYY-MM (YYYY 2010-2019, MM 01-12)

b. copy files from Data to Backup folder

```bash
#!/usr/bin/env bash

path="/workspaces/bash_learning_stuff/ex_files_bash/excercise_files/Ch03"
dir_data_name="data_directory"
dir_backup_name="backup_directory"

cd $path
mkdir $dir_data_name
mkdir $dir_backup_name

touch $path/$dir_data_name/Backup-201{0..9}-{0{1..9},1{0..2}}-{0..30}.tar.bz2
mkdir $path/$dir_backup_name/d201{0..9}-{0{1..9},1{1..2}}
```
```bash
#!/usr/bin/env bash

declare path="/workspaces/bash_learning_stuff/ex_files_bash/excercise_files/Ch03/copy"
declare path2="/workspaces/bash_learning_stuff/ex_files_bash/excercise_files/Ch03/daymonth"

cd $path

for i in Backup-201{1..9}-{0{1..9},1{0..2}}-{1..30}.tar.bz2 ; do

declare s="d"${i:7:7}

cp -v $i $path2/$s ; done
```


2. directory tree

```bash
 mkdir -p {sales,engineering,production,development}/{manager,employer{1,2,3}} 

# nesteddaymonth/
#├── development
#│   ├── employer1
#│   ├── employer2
#│   ├── employer3
#│   └── manager
#├── engineering
#│   ├── employer1
#│   ├── employer2
#│   ├── employer3
#│   └── manager
#├── production
#│   ├── employer1
#│   ├── employer2
#│   ├── employer3
#│   └── manager
#└── sales
#    ├── employer1
#    ├── employer2
#    ├── employer3
#    └── manager

```

# REGULAR EXPRESSIONS
https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/x11655.htm

```bash
.       pattern

[abc]   one character in list

[^abc]  one character not in list

[0-9]   one number in range

[:alpha:]   one character in class /upperorlowercase letter

 grep [abc] words.txt | head -n 3
#aaa
#Aaberg
#Aachen

 grep [^abc] words.txt | head -n 3
#12-point
#16-point
#18-point
```
matching occurences
```bash
.   one character
.?  zero/one occurrence
.+  one/more occurrence
```
find 150
```bash
#150 or 100-149 or 0 - 99
^(150|1[0..4][0..9]|[0..9][0..9]?)$ 
```



pattern matching GLOB vs REGEX / glob-files, regex-text
```bash
#!/bin/bash

cd backupfiles
shopt -s extglob

XGLOB='@(Archive|Backup)-[0-9][0-9][0-9][0-9]-[0-9][0-9]-@([0-9]|[0-9][0-9])@(@(.bak|.tar)?(.bz2|.gz|.xz)|.tgz)'

REGEX='^(Archive|Backup)-[0-9]{4}-[0-9]{2}-[0-9]{1,2}((.bak|.tar)(.bz2|.gz|.xz)|.tgz)?'

for FILE in * ;do
    if [[ $FILE =~ $REGEX ]] ;then
        echo "$FILE matches the regex"
    fi
done


#for FILE in * ;do
#    if [[ $FILE == $XGLOB ]] ;then
#        echo "$FILE matches the extended glob"
#    fi
#done

```

3. find credit card number in csv, find card type to which numer belongs

sales.csv
```csv
1/21/09 14:25,Product1,Tricia,Castricum,Noord-Holland,Netherlands,12/28/07 15:28,Diners Club,30203258689359
1/18/09 16:50,Product1,Celina,North Brunswick ,NJ,United States,1/18/09 16:25,Discover,6011033778582341
1/21/09 12:08,Product2,Rosemary,Jacksonville ,FL,United States,1/21/09 11:39,MasterCard,5440559871718716
1/22/09 6:41,Product1,Patrick,Baytown ,TX,United States,1/22/09 4:32,Visa,4539417253074221
1/12/09 9:23,Product1,Jacob,Winter Haven ,FL,United States,1/10/09 14:55,American Express,378116255997205
1/22/09 8:23,Product1,elisabeth,Gonzaga Univ ,WA,United States,1/22/09 7:55,Diners Club,30120067394890
1/21/09 2:15,Product1,Kevin ,London,England,United Kingdom,1/8/09 2:50,MasterCard,5200039383402943
1/16/09 1:07,Product2,Lesley,Cork,Cork,Ireland,1/14/09 4:10,American Express,348964412426239
1/20/09 8:51,Product1,Marie,Winchester ,MA,United States,7/23/08 14:59,Diners Club,30027146270100
1/23/09 3:33,Product2,Anja Langer,Saint Paul ,MN,United States,1/23/09 3:00,Visa,4485992744213764
1/23/09 3:30,Product1,Larry,Naarden,Noord-Holland,Netherlands,1/23/09 3:27,American Express,348605573992424
1/10/09 4:04,Product1,Jessica,Oldenburg,Lower Saxony,Germany,12/20/08 8:41,Diners Club,30181920069921
```

```bash
#!/bin/bash

path="/workspaces/bash_learning_stuff/ex_files_bash/excercise_files/Ch05"
input="/workspaces/bash_learning_stuff/ex_files_bash/excercise_files/Ch05/sales.csv"

read -p 'Credit card number: ' usernumb
cd $path

while IFS= read -r line
do
    if [[ "$usernumb" == "$(echo $line | grep -o '[^,]*$')" ]] ; then
            echo $(cut -d, -f8,9 <<< $line)
        fi

done < "$input"

# SPLIT CSV FILE - ONLY TWO LAST COLUMNS
# cut -d, -f8 < sales.csv  | cut -d, -f9 < sales.csv 

# SPLIT STRING , ONLY TWO LAST "COLUMNS" ' , '
# cut -d, -f8,9 <<< $line

# FROM LEFT TO FIRS ' , '
#echo "1/25/09 19:59,Product1,Kim,Seattle ,WA,United States,8/13/08 18:27,Discover,6011782142098570" | grep -o '[^,]*$' 

# READ LINE, SPLIT STRING FROM LEFT TO THE FIRST ' , '
#  numb_credit_card=$(echo $line | grep -o '[^,]*$')

```

3.1 find all VISA type cards, and their numbers

```bash
#!/bin/bash

#echo "1/25/09 19:59,Product1,Kim,Seattle ,WA,United States,8/13/08 18:27,Discover,6011782142098570" | grep -o '[^,]*$'
path="/workspaces/bash_learning_stuff/ex_files_bash/excercise_files/Ch05"
input="/workspaces/bash_learning_stuff/ex_files_bash/excercise_files/Ch05/sales.csv"


while read line
do
    if [[ $line =~ .*[Vv]isa.* ]] ; then
    echo "Record is : $(cut -d, -f8,9 <<< $line ) " 
    fi
done < sales.csv


#  .*[Vv]isa*.   | .*[Mm]aster[Cc]ard.*
# =~ compare strings
# .* (dot and asterisk) is used to match any string, equivalent to * in standard wildcards.
```