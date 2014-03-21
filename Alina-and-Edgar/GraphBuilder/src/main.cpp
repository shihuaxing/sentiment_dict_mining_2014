#include <iostream>
#include <fstream>
#include <cstdio>
#include <cstdlib>
#include <map>
#include <utility>
#include <string>

void clean_string(std :: string& s){
    for (std :: string :: iterator i = s.begin(); i != s.end(); ++i){
        if ( *i == '(' || *i == ')' || *i == '\'' || *i == ',' || *i == ']' || *i == '[' ){
            i = s.erase(i);
            --i;
        }
    }
}

int main(int argc, char** argv){    
    if (argc != 3){        
        std :: cerr << "Usage: GraphBuilder.exe input_file output_file" << std :: endl;    
    } else {        
        const char* input_file = argv[1];
        const char* output_file = argv[2];
        std :: ifstream ifs(input_file, std :: ifstream :: in);
        std :: ofstream ofs(output_file, std :: ifstream :: out);
        std :: map<std:: string, std :: map<std :: string, std :: pair<int, int> > > graph;
        while (!ifs.eof()){          
            std :: string first_adj, second_adj, num;
            ifs >> first_adj >> second_adj >> num;
            clean_string(first_adj);
            clean_string(second_adj);
            clean_string(num);
            int polarity = atoi(num.c_str());
            if (graph.find(first_adj) == graph.end()){          		
          		if (polarity > 0){			
					graph[first_adj][second_adj] = std :: make_pair(polarity, 0);
          		} else {
          			graph[first_adj][second_adj] = std :: make_pair(0, polarity);
          		}
            } else {
            	if (graph[first_adj].find(second_adj) == graph[first_adj].end()){
            		if (polarity > 0){
						graph[first_adj][second_adj] = std :: make_pair(polarity, 0);
          			} else {
          				graph[first_adj][second_adj] = std :: make_pair(0, polarity);          		
          			}
            	} else {
            		int pos_polarity = graph[first_adj][second_adj].first;
            		int neg_polarity = graph[first_adj][second_adj].second;
            		if (polarity > 0){
						graph[first_adj][second_adj] = std :: make_pair(pos_polarity + polarity, neg_polarity);
          			} else {         			
          				graph[first_adj][second_adj] = std :: make_pair(pos_polarity, neg_polarity + polarity);
           			}
          		}
            }
        }
        std :: map<std :: string, std :: map<std :: string, std :: pair<int, int> > > :: iterator it;
        for (it = graph.begin(); it != graph.end(); ++it){
            std :: map<std :: string, std :: pair<int, int> > :: iterator v_it;
            ofs << it->first << ": ";
            for (v_it = it->second.begin(); v_it != it->second.end(); ++v_it){
                ofs << "{" << v_it->first << ": " << v_it->second.first << ", " << v_it->second.second << "}; ";
            }
            ofs << std :: endl;
        }
        ifs.close();
        ofs.close();
    }
    return 0;
}