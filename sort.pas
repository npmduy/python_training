program test;
type mang = array[1..20] of longint;
var m1,m2:mang;
    spt,i,a,NN,bien,spt2,LN:integer;
begin
spt:=5;
spt2:=5;
m1[1]:=5;
m1[2]:=2;
m1[3]:=2;
m1[4]:=4;
m1[5]:=4;

for i:=1 to spt do
    begin
        NN:=m1[i];
        LN:=m1[i];
        for a:=1 to spt2 do
            begin
                if m1[a]<NN then NN:=m1[a];
                if m1[a]>LN then LN:=m1[a];
            end;
        for a:=1 to spt2 do
            if m1[a]=NN then
                begin
                    m1[a]:=LN+1;
                    break;
                end;
        m2[i]:=NN;
    end;
for i:=1 to spt do writeln(m2[i]);
readln;
end.