Role Name
=========

## Запуск плейбуков

* Для создания кубкластера на серверах выполните сначала роль prepare-k8s, а потом k8s. Роль prepare-k8s надо выполнять из под root юзера, а роль k8s нужно выполнять от своего юзера, примеры ниже.
  Пример:
  ```
  ansible-playbook -u root --become --become-user=root 02_1_k8s3.yml -K -k -i hosts
  ansible-playbook -u v.izvekov --become --become-user=root 02_2_k8s3.yml -K -k -i hosts
  ```
* Для корркного выпонения роли, control ноды должны быть в группе k8s-controls, worker ноды должны быть в группе k8s-workers, эти группы должны быть в группе k8s-nodes
