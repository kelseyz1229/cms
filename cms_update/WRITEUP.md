# Write-up Template

### Analyze, choose, and justify the appropriate resource option for deploying the app.

*For **both** a VM or App Service solution for the CMS app:*
- *Analyze costs, scalability, availability, and workflow*
- *Choose the appropriate solution (VM or App Service) for deploying the app*
- *Justify your choice*

##Cost:  
VMs tend to be more expensive because they offer full control and incur provisioning costs. You are charged for the VM whether it is actively used or not, leading to potentially higher costs if the VM remains idle.
App service is more economical, with a pay-as-you-go model. It's ideal when full control over the environment isn't necessary. The cost is based on the application's usage, making it a cost-effective solution for variable workloads.
Scalability: 
Vm requires manual scaling management, including configuring scale sets and setting up auto-scaling rules. This process can be both complex and time-consuming.
App service has a built-in auto-scaling capabilities, both vertical and horizontal. Vertical scaling adjusts resources within a single instance, billed according to the app service plan tier. Horizontal scaling modifies the number of VM instances while the app is active, facilitating easy workload management without manual intervention.
Availability: 
Using vm, developers must manage availability due to the full control over the environment, including tasks like setting up load balancers and implementing failover mechanisms.
App service comes with built-in high availability and failover features, reducing the need for extensive manual setup. This allows developers to concentrate more on the application rather than the underlying infrastructure.
Workflow: 
Vm provides comprehensive control over the environment, necessitating detailed configuration. Suitable for applications with specific requirements that need custom configurations.
App service has a managed platform that comes with built-in features. This enables developers to focus on writing code rather than managing infrastructure. Ideal for applications that benefit from automated tasks such as OS updates and security patches.

I choose App Service for deploying the app because it is more cost-effective compared to a Virtual Machine (VM), which is generally more expensive and offers full access. App Service provides high availability and supports both vertical and horizontal auto-scaling, ensuring the app can handle varying loads efficiently. Additionally, it allows for continuous deployment using GitHub, streamlining the development process. Given that this is a lightweight application and service, App Service is the better choice, offering essential features without the higher cost and complexity of managing a VM.



### Assess app changes that would change your decision.

*Detail how the app and any other needs would have to change for you to change your decision in the last section.* 

##If the application requires more complex features and configurations, a VM (Virtual Machine) would be the preferable choice due to the necessity for full control. Additionally, for applications with a heavy load, a VM will be more suitable to meet the demand.

