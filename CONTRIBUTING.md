# Contributing to CovidKenya/core

Thank you for showing interest in contributing to CovidKenya/core. Following these guidelines help to communicate that you respect the time of the developers managing and working on this open source project. In return, they should reciprocate that respect in addressing your issue, assessing changes and also helping you finalise your pull requests.

### What do I do? How do I get started?

Follow the [README.md](/README.md) guide. If you've noticed a bug, want to add a feature or have a question, [search the issue tracker](https://github.com/CovidKenya/core/issues) to see if someone else already created a ticket. If that has not yet been done, go ahead and [make one](https://github.com/CovidKenya/core/issues/new).

### Clone & create a branch

If this is something you think you can fix, [clone CovidKenya/core](https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository) and create a branch with a descriptive name. Always checkout from the **staging branch**, that is the default and up-to-date branch.

A good branch name would be:

```sh
git checkout -b 13-fix-cta-button
```

### Implement your fix or feature

At this point, you're ready to make your changes. Feel free to ask for help; everyone was once a beginner; everyone is learning.

The [requirements](/requirements.txt) file contain the packages and dependencies to be installed and set up.

Please ensure that the issue you've fixed is related to the branch you're currently working from. If you want to fix something else unrelated to whatever you've worked on, do another checkout from the staging branch and give the new branch an appropriate name.This makes it easy for the maintainers to track your fixes.

#### Commits
The goal is that each commit has a **single focus**. Each commit should record a single-unit change. Now this can be a bit subjective (which is totally fine), but each commit should make a change to just one aspect of the project.

Conversely, a commit shouldn't include unrelated changes - changes to the sidebar and rewording content in the footer. These two aren't related to each other and shouldn't be included in the same commit. Work on one change first, commit that, and then change the second one. That way, if it turns out that one change had a bug and you have to undo it, you don't have to undo the other change too.

If you have to use "and" in your commit message, your commit is probably doing too many changes - break the changes into separate commits

#### Commits Message
Explain what the commit does (not how or why).

### Keeping your Pull Request updated

Related to the above, if a maintainer asks you to "rebase" your PR, they're saying that a lot of code has changed, and that you need to update your branch so it's easier to merge.

### Merging a PR (for maintainers only)

A PR can only be merged into staging by a maintainer if:

- It has no requested changes
- It is up-to-date with current staging branch
- It is a valid fix/feature.

Any maintainer is allowed to merge a PR if all of these conditions are met.
