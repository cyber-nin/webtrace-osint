from app.modules.graph_engine import build_graph

def run_worker():
    graph = build_graph()
    print("[+] Graph built:", graph.number_of_nodes())

if __name__ == "__main__":
    run_worker()
