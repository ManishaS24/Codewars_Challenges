# include <iostream>
using namespace std;

class Flower{
    private:
        string flower_name;
        int num_of_pedals;
        float cost;
    //constructor method
    public :
        Flower(){
            string flower_name = "";
            int num_of_pedals = 0;
            float cost = 0.0;
        }
        Flower(string flower_name, int num_of_pedals, float cost){
            this -> flower_name = flower_name;
            this -> num_of_pedals = num_of_pedals;
            this -> cost = cost;
        }

    // setter methods
    public:
        void set_name(string flower_name){
            this -> flower_name = flower_name;
        }
        string set_pedals(int num_of_pedals){
            this -> num_of_pedals = num_of_pedals;
        }
        string set_cost(float cost){
            this -> cost = cost;
        }

    //getter methods
        string get_name(){
            return flower_name;
        }
        int get_num_of_pedals(){
            return num_of_pedals;
        }
        float get_cost(){
            return cost;
        }
};

int main(){
    Flower f("Rose", 10, 20.5);
    
    cout << f.get_name() << endl;
    cout << f.get_num_of_pedals() << endl;
    cout << f.get_cost() << endl;

    f.set_cost(75.21);
    cout << "Updated price: " << f.get_cost() << endl;


}