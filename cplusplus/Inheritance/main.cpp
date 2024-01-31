#include <iostream>

using namespace std;

class vechical{
public:
    vechical()
    {
    cout<<"This a first base class"<<endl;
    }
    };
    class twowheeler{
public:
    twowheeler()
    {

        cout<<"this is a second base class"<<endl;

    }
    };

    class car:
        public vechical,public twowheeler{
        };
        int main()
        {

           car obj;
            return 0;
        }

