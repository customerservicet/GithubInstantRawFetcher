# GithubInstantRawFetcher
It allows you to fetch the updates you made on the file, instantly.

# main.py
import github_data

if __name__ == "__main__":    
    githubData = github_data.GithubData(True) # True defines if it should set self.data

    githubData.fetch("https://github.com/customerservicet/deneme/blob/main/deneme.txt")

    githubData.turn_to_value(githubData.data)

    print(githubData.data)
