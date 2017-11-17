#include <cstdio>

using namespace std;
char s[100000];
int position=0;
int term();
int factor();
int expression()
{
    int value=term();
    while(s[position]=='+' || s[position]=='-')
    {
        if(s[position]=='+')
        {
            position++;
            value=value+term();
        }
        if(s[position]=='-')
        {
            position++;
            value=value-term();
        }
    }
    return value;
}
int term()
{
    int value=factor();
    while(s[position]=='*' || s[position]=='/')
    {
        if(s[position]=='*')
        {
            position++;
            value=value*factor();
        }
        if(s[position]=='/')
        {
            position++;
            value=value/factor();
        }
    }
    return value;
}
int factor()
{
    int value=0,sign=1;
    while(s[position]=='-')
    {
        position++;
        sign=-sign;
    }
    if(s[position]=='(')
    {
        position++;
        value=expression();
        position++;
        return value*sign;
    }
    while(s[position]>='0' && s[position]<='9')
    {
        value=value*10+(s[position]-'0');
        position++;
    }
    return value*sign;
}
int main()
{
    FILE *in,*out;
    in=fopen("evaluation.in","r");
    out=fopen("evaluation.out","w");
    int result;
    fscanf(in,"%s",&s);
    result=expression();
    fprintf(out,"%d",result);
    return 0;
}
