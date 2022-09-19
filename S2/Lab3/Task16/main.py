import datastructures as ds


class ProcedureGraph(ds.OrientedGraph):
    searching_procedure = None
    visited = []

    def __init__(self, input_filename):
        input_file = open(input_filename, "r")

        self.build_procedure_graph(input_file)

        input_file.close()

    def line_handler(self, line):
        if line[-1] == "\n":
            line = line[:line.index("\n")]
        return line

    def build_procedure_graph(self, input_file):
        first_line_flag = False
        main_procedure_flag = True
        value_of_sub_proc_flag = True
        main_procedure = ""

        for line in input_file:
            line = self.line_handler(line)

            if first_line_flag is False:
                first_line_flag = True
                continue

            if main_procedure_flag:
                main_procedure = line
                self.graph[main_procedure] = []
                main_procedure_flag = False
                continue

            if line[0] == "*":
                value_of_sub_proc_flag = True
                main_procedure_flag = True
                continue

            if main_procedure_flag is False and value_of_sub_proc_flag:
                value_of_sub_proc_flag = False
                continue

            if main_procedure_flag is False and value_of_sub_proc_flag is False:
                self.graph[main_procedure].append(line)

    def calling_chain(self, procedure):
        sub_procedures = self.graph.get(procedure, None)

        if sub_procedures is not None:
            if self.searching_procedure in sub_procedures:
                return True
            else:
                for sub_p in sub_procedures:
                    if sub_p not in self.visited:
                        self.visited.append(sub_p)
                        return self.calling_chain(sub_p)

        return False

    def is_recursive(self):
        for main_procedure in self.graph.keys():
            self.searching_procedure = main_procedure
            self.visited = []

            if self.calling_chain(main_procedure) is True:
                print(main_procedure, "is Yes")
            else:
                print(main_procedure, "is NO")


p_graph = ProcedureGraph("input")
p_graph.is_recursive()

