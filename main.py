import github_data

if __name__ == "__main__":    
    githubData = github_data.GithubData(True)

    githubData.fetch("https://github.com/customerservicet/deneme/blob/main/deneme.txt")

    githubData.turn_to_value(githubData.data)

    print(githubData.data)