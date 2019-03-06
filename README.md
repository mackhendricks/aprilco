#Setup Vault

1. Download Vault from https://www.vaultproject.io/downloads.html

2. Install Vault

3. Configure Vault

```
vault secrets enable pki
vault secrets tune -max-lease-ttl=87600h pki
vault write pki/root/generate/internal common_name=myvault.com ttl=87600h
vault write pki/roles/example-dot-com     allowed_domains=example.com     allow_subdomains=true max_ttl=72h
vault write pki/issue/example-dot-com common_name=aprilco.example.com
```

4. Deploy Application that uses the secrets
