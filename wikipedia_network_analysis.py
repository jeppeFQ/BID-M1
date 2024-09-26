import wikipediaapi
import networkx as nx
import pandas as pd  
import sys

# Sæt brugeragenten
user_agent = "WikipediaFetcher/1.0 (myemail@example.com)"

# Initialiser Wikipedia API med brugeragenten
wiki = wikipediaapi.Wikipedia(
    language='en',
    extract_format=wikipediaapi.ExtractFormat.WIKI,
    user_agent=user_agent
)

def get_links(page_title, depth=1):
    """Hent links fra en Wikipedia-side op til en bestemt dybde."""
    page = wiki.page(page_title)

    # Tjek om siden eksisterer
    if not page.exists():
        return {}

    links = {page_title: list(page.links.keys())}

    if depth > 1:
        # Hent links fra de forbundne sider rekursivt
        for link in links[page_title]:
            links.update(get_links(link, depth - 1))

    return links

def main(page_title, depth, num_nodes, num_edges):
    # Hent interne links fra den angivne artikel
    links = get_links(page_title, depth)

    # Opret en graf fra de hentede links
    G = nx.Graph()

    # Tilføj noder og edges til grafen
    for article, linked_articles in links.items():
        for linked_article in linked_articles:
            G.add_edge(article, linked_article)

    # Print de første num_nodes og num_edges fra grafen
    print("Første {} noder i grafen:".format(num_nodes))
    for node in list(G.nodes())[:num_nodes]:  # Slicing for at få de første num_nodes
        print(f"- {node}")

    print("\nFørste {} kanter i grafen:".format(num_edges))
    for edge in list(G.edges())[:num_edges]:  # Slicing for at få de første num_edges
        print(f"- {edge}")

    # Beregn og print betweenness centrality
    betweenness_centrality = nx.betweenness_centrality(G)
    sorted_betweenness = sorted(betweenness_centrality.items(), key=lambda x: x[1], reverse=True)

    print("\nTop 5 artikler efter betweenness centrality:")
    for page, centrality in sorted_betweenness[:5]:
        print(f"{page}: {centrality}")

    # Gem edgelist som en CSV-fil
    edge_list = G.edges(data=True)
    edge_df = pd.DataFrame(edge_list, columns=['Kilde', 'Mål', 'Attributter'])
    edge_df.to_csv('edge_list.csv', index=False)

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Brug: python script.py <Wikipedia_Side_Titel> <Dybde> <Antal_Noder> <Antal_Kanter>")
        sys.exit(1)

    # Læs argumenter fra kommandolinjen
    page_title = sys.argv[1]
    depth = int(sys.argv[2])
    num_nodes = int(sys.argv[3])
    num_edges = int(sys.argv[4])

    # Kør hovedfunktionen
    main(page_title, depth, num_nodes, num_edges)
