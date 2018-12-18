# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities, tables

class Service(pulumi.CustomResource):
    """
    Manages an Azure Container Service Instance
    
    ~> **NOTE:** All arguments including the client secret will be stored in the raw state as plain-text.
    [Read more about sensitive data in state](https://www.terraform.io/docs/state/sensitive-data.html).
    
    ~> **DEPRECATED:** [Azure Container Service (ACS) has been deprecated by Azure in favour of Azure (Managed) Kubernetes Service (AKS)](https://azure.microsoft.com/en-us/updates/azure-container-service-will-retire-on-january-31-2020/). Support for ACS will be removed in the next major version of the AzureRM Provider (2.0) - and we **strongly recommend** you consider using Azure Kubernetes Service (AKS) for new deployments.
    
    ## Example Usage (DCOS)
    
    ```hcl
    resource "azurerm_resource_group" "test" {
      name     = "acctestRG1"
      location = "West US"
    }
    
    resource "azurerm_container_service" "test" {
      name                   = "acctestcontservice1"
      location               = "${azurerm_resource_group.test.location}"
      resource_group_name    = "${azurerm_resource_group.test.name}"
      orchestration_platform = "DCOS"
    
      master_profile {
        count      = 1
        dns_prefix = "acctestmaster1"
      }
    
      linux_profile {
        admin_username = "acctestuser1"
    
        ssh_key {
          key_data = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCqaZoyiz1qbdOQ8xEf6uEu1cCwYowo5FHtsBhqLoDnnp7KUTEBN+L2NxRIfQ781rxV6Iq5jSav6b2Q8z5KiseOlvKA/RF2wqU0UPYqQviQhLmW6THTpmrv/YkUCuzxDpsH7DUDhZcwySLKVVe0Qm3+5N2Ta6UYH3lsDf9R9wTP2K/+vAnflKebuypNlmocIvakFWoZda18FOmsOoIVXQ8HWFNCuw9ZCunMSN62QGamCe3dL5cXlkgHYv7ekJE15IA9aOJcM7e90oeTqo+7HTcWfdu0qQqPWY5ujyMw/llas8tsXY85LFqRnr3gJ02bAscjc477+X+j/gkpFoN1QEmt terraform@demo.tld"
        }
      }
    
      agent_pool_profile {
        name       = "default"
        count      = 1
        dns_prefix = "acctestagent1"
        vm_size    = "Standard_F2"
      }
    
      diagnostics_profile {
        enabled = false
      }
    
      tags {
        Environment = "Production"
      }
    }
    ```
    """
    def __init__(__self__, __name__, __opts__=None, agent_pool_profile=None, diagnostics_profile=None, linux_profile=None, location=None, master_profile=None, name=None, orchestration_platform=None, resource_group_name=None, service_principal=None, tags=None):
        """Create a Service resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not agent_pool_profile:
            raise TypeError('Missing required property agent_pool_profile')
        __props__['agent_pool_profile'] = agent_pool_profile

        if not diagnostics_profile:
            raise TypeError('Missing required property diagnostics_profile')
        __props__['diagnostics_profile'] = diagnostics_profile

        if not linux_profile:
            raise TypeError('Missing required property linux_profile')
        __props__['linux_profile'] = linux_profile

        if not location:
            raise TypeError('Missing required property location')
        __props__['location'] = location

        if not master_profile:
            raise TypeError('Missing required property master_profile')
        __props__['master_profile'] = master_profile

        __props__['name'] = name

        if not orchestration_platform:
            raise TypeError('Missing required property orchestration_platform')
        __props__['orchestration_platform'] = orchestration_platform

        if not resource_group_name:
            raise TypeError('Missing required property resource_group_name')
        __props__['resource_group_name'] = resource_group_name

        __props__['service_principal'] = service_principal

        __props__['tags'] = tags

        super(Service, __self__).__init__(
            'azure:containerservice/service:Service',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

