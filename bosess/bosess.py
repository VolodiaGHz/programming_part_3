def read_file(file):
    file = open(file, 'r')
    file_data = file.read()
    file.close()
    return file_data


def worker_vertex(data_of_vertex):
    list_of_vertex = []
    for num in range(len(data_of_vertex.split(' ')[0])):
        list_of_vertex.append(num)
    return list_of_vertex


def worker(data_of_vertex):
    list_worker = []
    for tally in data_of_vertex.split(' '):
        links_employee = []
        for i in range(len(tally)):
            if tally[i] == 'Y':
                links_employee.append(i)
        if not links_employee:
            list_worker.append([])
        else:
            list_worker.append(links_employee)
    print(list_worker)
    return list_worker


def get_graph(list_of_vertex, certificates):
    graph = {}
    for i in range(len(list_of_vertex)):
        graph[list_of_vertex[i]] = certificates[i]
    return graph


def work_status(graph_worker):
        for worker in range(len(graph_worker)):
            if not graph_worker[worker]:
                print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
                print(str(worker) + " no manager")
                print("Salary of " + str(worker) + " = 1 ")
            else:
                for subordinate in graph_worker[worker]:
                    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
                    print(str(worker) + "  manager for " + str(subordinate))
                    print("Salary of " + str(worker) + " = " + str(subordinate))


if __name__ == '__main__':
    data_file = read_file("input")
    list_vertex = worker_vertex(data_file)
    list_worker = worker(data_file)
    graph_emloyee = get_graph(list_vertex, list_worker)
    work_status(graph_emloyee)

