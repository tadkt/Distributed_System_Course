Collaborating on GitHub with a group where the group captain manages merge requests is a good way to maintain a structured workflow. Here's a step-by-step guide:

---

### 1. **Setup the Central Repository**
- The group captain creates a repository on GitHub (the **central repository**).
- Add all group members as **collaborators** with at least read access to the repository.

---

### 2. **Fork the Central Repository**
- Each group member forks the central repository into their own GitHub account. This creates a personal copy of the repository where members can freely work without affecting the central repository.

---

### 3. **Clone the Forked Repository**
- Each member clones their forked repository to their local machine:
  ```bash
  git clone https://github.com/<your-username>/<forked-repo>.git
  ```

---

### 4. **Set Up Remote Connections**
- To keep their fork in sync with the central repository, each member adds the central repository as an additional remote:
  ```bash
  git remote add upstream https://github.com/<captain-username>/<central-repo>.git
  ```

- Confirm the remotes with:
  ```bash
  git remote -v
  ```

---

### 5. **Work on a Feature Branch**
- Each member creates a new branch for their task:
  ```bash
  git checkout -b feature/<feature-name>
  ```

- They make changes, commit them, and push the branch to their forked repository:
  ```bash
  git push origin feature/<feature-name>
  ```

---

### 6. **Submit a Pull Request**
- After completing their task, members create a pull request (PR) to merge their branch into the **central repository**:
  1. Go to your fork on GitHub.
  2. Navigate to the branch you worked on.
  3. Click **"Pull Request"**.
  4. Choose the **central repository** as the base and the feature branch from your fork as the compare.
  5. Add a title, description, and any required details, then submit the pull request.

---

### 7. **Group Captain Reviews and Merges PRs**
- The group captain reviews each pull request, suggests changes if needed, and merges only when the work meets the group's standards.
- To merge:
  1. Navigate to the pull request.
  2. Click **"Merge Pull Request"**.
  3. Use options like "Squash and Merge" or "Rebase and Merge" to maintain a clean commit history.

---

### 8. **Syncing with the Central Repository**
- Members keep their forks up-to-date with the central repository by pulling changes:
  ```bash
  git fetch upstream
  git merge upstream/main
  ```

- Push updates to their fork if necessary:
  ```bash
  git push origin main
  ```

---

### 9. **Repeat the Process**
- For new tasks, repeat steps 4–8. Each member works on their feature branch, submits pull requests, and the captain manages merges.

---

### Best Practices
- **Write clear commit messages**: Explain what changes you made.
- **Test code before creating a PR**: Ensure changes don’t break the codebase.
- **Use code reviews**: The captain can review PRs with tools like GitHub suggestions to maintain quality.
- **Update your branches**: Frequently pull changes from the central repository to avoid conflicts.

By using this workflow, you'll maintain a clear and structured process where the group captain manages all code integration, reducing potential issues and conflicts.
