Related resources:

- https://www.cbtnuggets.com/blog/certifications/open-source/linux-hard-links-versus-soft-links-explained
- https://www.baeldung.com/linux/bind-mounts

Types:

* Soft links = like regular anchors to folders, they imitate path resolution to different folder which is enough for Terraform like tool, but Git will see only one file instead of folder
  * ln -s source target # create
  * rm target # delete
* Hard Links = Making fully fledged mirrored files. U can even delete original. As long as any hard link is left for file, it is still existing. Real time sync. Because link links to memory in hard drive. Disadvantage: For file only.
  * ln source target # create
  * ls -l # check
  * rm target # delete
* Mount --bind = The best option when u deal with multiple projects/microservices, u can bind entire projects for real time syncronization (almost same like pip install -e, installing some local package in editing mode essentially) (Very useful to have multiple projects combined into one project temporally) (Even git can see those mounted folders fully, so u can commit those files as long as they are mounted)
  * findmnt --real # discovering mounts
  * mount --bind source_path target_path # binding folder to folder
  * umount target_path # unbinding folder
