from scholarly import scholarly
import igraph



class LitGraph(igraph.Graph):
    def __init__(self):
        igraph.Graph.__init__(self, directed=True)

    def add_article(self, doi=None):
        # Searching by DOI is unambiguous
        # Should check for ambiguity - i.e., does the search return more than one result?

        if doi:
            query = scholarly.search_pubs(str(doi))
            # A DOI looks like "10.1016/S0924-4247(01)00803-2"
            try:
                result = next(query)
                pub = result['bib']
                attributes = {
                    'title': pub['title'],
                    'author': pub['author'],
                    'year': pub['pub_year'],
                    'abstract': pub['abstract'],
                    'venue': pub['venue'],
                    'url': result['pub_url'],
                    'citations': result['num_citations']
                }

                Authors = pub['author'][0] if len(pub['author'])<=1 else pub['author'][0] + ' et. al.'
                vertex_name = pub['title'] + ': ' + Authors
                self.add_vertex(name=vertex_name, **attributes)

                return vertex_name
            except(StopIteration):
                print(f'No search results for query "{doi}"')



if __name__ == '__main__':
    # query = scholarly.search_pubs('fdkslfskdlfjklsdfjsdklfsdjklfsdjsklsj')
    # print(next(query))


    lg = LitGraph()
    new_vertex = lg.add_article(doi='10.1016/S0924-4247(01)00803-2')
    print(new_vertex)
