# File permissions in Linux

## Project description

In this project, I used Linux commands to examine and manage file permissions in a research team's file system. My objective was to verify that each file and directory had the appropriate authorization, remove unauthorized access, and apply the principle of least privilege to improve the security of the system.

## Check file and directory details

To examine the permissions of all files, including hidden files, I navigated to the **projects** directory and used the following commands:

```bash
cd /home/researcher2/projects
ls -la
```

The `ls -la` command displays all files and directories, including hidden files, along with detailed information such as ownership, permissions, file size, and modification date.

Example output:

```text
-rw-rw-r--  project_k.txt
-rw-rw-rw-  project_t.txt
-rw-r-----  project_m.txt
-rw-rw-r--  .project_x.txt
drwxr-x---  drafts
```

## Describe the permissions string

Example permission string:

```text
-rw-rw-r--
```

Explanation:

* **-** : Regular file
* **rw-** : The owner has read and write permissions.
* **rw-** : The group has read and write permissions.
* **r--** : Other users have read-only permission.

The 10-character permission string identifies the file type and the permissions assigned to the owner, group, and other users. It helps security professionals verify whether access rights comply with organizational security policies.

## Change file permissions

The organization does not allow **other users** to have write permission on any file. I identified the file with incorrect permissions and removed the write permission for others using:

```bash
chmod o-w project_t.txt
```

Verification:

```bash
ls -l project_t.txt
```

After the change, the file no longer grants write access to other users, reducing the risk of unauthorized modifications.

The restricted file **project_m.txt** should only be readable and writable by its owner. To remove read and write permissions from the group, I used:

```bash
chmod g-rw project_m.txt
```

Verification:

```bash
ls -l project_m.txt
```

The file is now accessible only by its owner, protecting sensitive information.

## Change file permissions on a hidden file

The hidden file **.project_x.txt** is archived and should not be modified by anyone. The owner and group should only have read permission.

Command used:

```bash
chmod u-w,g-w .project_x.txt
```

Verification:

```bash
ls -la .project_x.txt
```

This configuration prevents accidental or unauthorized modifications while still allowing authorized users to read the archived file.

## Change directory permissions

Only the **researcher2** user should be able to access the **drafts** directory. To remove execute permission from the group, I used:

```bash
chmod g-x drafts
```

Verification:

```bash
ls -ld drafts
```

After this change, members of the group can no longer enter or access the contents of the **drafts** directory, ensuring that only the owner has access.

## Summary

In this project, I examined file and directory permissions using the `ls -la` command and modified permissions using the `chmod` command. I secured regular files, hidden files, and directories by removing unnecessary permissions and enforcing the principle of least privilege. These tasks demonstrate essential Linux system administration and cybersecurity skills used to protect sensitive information from unauthorized access.
