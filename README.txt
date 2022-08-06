# coderebracket
A simple tool to reposition brackets in huge code bases:
it accepts as parameter the starting directory of the code base, otherwise it will use as root the directory from which it is invoked.

On the top of the script there is a list with all the extensions of the files to be modified,
it can be modified to act on different files depending on the case.

This tool is intended to be used for C and C++ codes.

This tool converts code from this format:

void func();
int main(){

  for(...){

    while(...){
         func();
      }
  }

  return 0;
}
void func(){
  ...
}

Into this format:

void func();
int main()
{

  for(...)
  {

    while(...)
    {
      func();
    }
  }

  return 0;
}
void func()
{
  ...
}
