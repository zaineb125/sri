import os


def read_file_content(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read().lower()

def search_files(search_term, search_type='keyword'):
    root_dir = "./ClassifiedFiles/"
    matching_files = []

    for root, dirs, files in os.walk(root_dir):
        for file in files:
            file_path = os.path.join(root, file)
            file_content = read_file_content(file_path)

            if search_type == 'keyword' and search_term.lower() in file_content:
                matching_files.append(file_path)
            
            
            elif search_type == 'multi-keyword':
                if all(term.lower() in file_content for term in search_term):
                    matching_files.append(file_path)
            
            
            elif search_type == 'content' and search_term.lower() in file_content:
                matching_files.append(file_path)

    return matching_files

def evaluate_search_results(matching_files, search_terms):
    evaluation_result = {
        "total_files_found": len(matching_files),
        "relevance_accuracy": 0.0
    }

    
    if isinstance(search_terms, str):
        search_terms = [search_terms]

    for file_path in matching_files:
        file_content = read_file_content(file_path)
        total_term_count = 0

        
        for term in search_terms:
            term_count = file_content.count(term.lower())
            total_term_count += term_count

        
        evaluation_result["relevance_accuracy"] += total_term_count

    if matching_files:
        evaluation_result["relevance_accuracy"] /= len(matching_files)

    return evaluation_result




search_term =["intégration","sécurité" ] 
search_type = "multi-keyword" 
matching_files = search_files(search_term, search_type)


evaluation = evaluate_search_results(matching_files, search_term)
print(evaluation)
print(matching_files)
