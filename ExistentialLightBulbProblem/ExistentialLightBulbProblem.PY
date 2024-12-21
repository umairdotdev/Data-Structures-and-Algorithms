# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 20:26:42 2020

@author: Lenovo
"""

problemSwitch=[]
#Function for getting data from instance files
def readFile(fileName):
    Input = open(fileName,'r')
    Data = []
    line=Input.readline()
    Data.append(line)
    while line!='':
        line=Input.readline()
        Data.append(line)
    finalData = []
    for i in Data:
        finalData.append(i.strip())
    
    finalData.pop(len(finalData)-1)
        
    numSwitches = int(finalData[0])
    listClauses=[]
    
    for i in finalData[2:]:
        listClauses.append(i)
        
    clauses=[]
    
    for i in listClauses:
        clauses.append(i.split())
    clausesTuples=[]
    
    for i in clauses:
        a=list(map(int, i))
        clausesTuples.append(tuple(a))
        
    return clausesTuples, numSwitches

#Function for running depth first search on the graph
def DepthFirstSearch(node, visited, graph):
    if visited[node]:
        return []
    visited[node] = True
    output = []
    for neighbour in graph[node]:
        output += DepthFirstSearch(neighbour, visited, graph)
    output.append(node)
    return output

#Build the components for the reverse graph 
def componentBuilding(node, C, visited, reversedGraph):
    print(node, end= ' ')
    if visited[node]:
        return C
    visited[node] = True
    if -node in C:
        global problemSwitch
        problemSwitch.append(node) #This is the variable which is the cause of no solution
        raise Exception()
    if node not in C:
        C[node] = True
    for neighbour in reversedGraph[node]:
        componentBuilding(neighbour, C, visited, reversedGraph)
    return C

#Solver function which takes a query along with the total number of variables
#Returns the solution if it exists otherwise returns None
def Solver(Q, n):
    graph = []
    reversedGraph = []
    
    for i in range((n+1)*2):
        graph.append([])
        reversedGraph.append([])
    for (a, b) in Q:
        graph[-a].append(b)
        graph[-b].append(a)
        reversedGraph[a].append(-b)
        reversedGraph[b].append(-a)
    visited_list = [False] * ((n+1)*2)
    order_list = []
    for i in range(n):
        order_list += DepthFirstSearch(i+1, visited_list, graph)
        order_list += DepthFirstSearch(-(i+1), visited_list, graph)
    order_list = order_list[::-1]
    visited_list = [False] * ((n+1)*2)
    
    components_list = []
    try:
        for node in order_list:
            components_list.append(componentBuilding(node, {}, visited_list, reversedGraph))
    except:
        return
    values_dict = {}
    while len(values_dict) < n:
        c = components_list.pop()
        for p in c:
            if abs(p) not in values_dict:
                values_dict[abs(p)] = abs(p) == p
    result=[]
    dict_items=values_dict.items()
    sorted_items=sorted(dict_items)
    for i in sorted_items:
        a,b=i
        if b==False:
            result.append(-a)
        else:
            result.append(a)
    return result

if __name__ == "__main__":
    count=0
    sol_instances=[]
    a,b=readFile('instance1.txt')
    print('\nThe path for building components for instance1 is:')
    sol_instances.append(Solver(a, b))
    
    a,b=readFile('instance2.txt')
    print('\nThe path for building components for instance2 is:')
    sol_instances.append(Solver(a, b))
    
    a,b=readFile('instance3.txt')
    print('\nThe path for building components for instance3 is:')
    sol_instances.append(Solver(a, b))
    
    a,b=readFile('instance4.txt')
    print('\nThe path for building components fpr instance4 is:')
    sol_instances.append(Solver(a, b))
    

    for i in range(len(sol_instances)):
        if sol_instances[i] != None:
            print('The solution for instance ', i+1,' is:' )
            for j in range(len(sol_instances[i])):
                print(sol_instances[i][j],end=" ")
        else:
            print('\nThere is no solution for instance ', i+1)
            print('The switch that caused problem is: ',problemSwitch[count])
            count=count+1
    
    
    while True:
        choice = None
        while choice is None:
            choice = input("\nDo you have another instance file(Type YES or NO): ")
        if choice=="YES":
            filename = None
            while filename is None:
                filename = input("\nEnter name of instance file(eg instance1.txt): ")
            a,b=readFile(filename)
            sol_user=Solver(a, b)
    
            if sol_user != None:
                print('The solution for input instance is:' )
                for j in range(len(sol_user)):
                    print(sol_user[j],end=" ")
            else:
                print('\nThere is no solution for input instance ')
                print('The switch that caused problem is: ',problemSwitch[count])
                count=count+1
                
        else:
            print('Program terminated successfuly')
            break
    
    
    
    
    
    