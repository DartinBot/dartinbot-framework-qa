# DartinBot Blockchain Development Template

<dartinbot-template 
    name="Blockchain Development Template"
    category="blockchain"
    version="3.0.0"
    framework-version="3.0.0"
    scope="blockchain-development-project"
    difficulty="advanced"
    confidence-score="0.90"
    auto-improve="true">

## Project Overview
<dartinbot-detect>
Target: Decentralized application development with smart contracts
Tech Stack: Solidity, Web3.js, Ethereum, Hardhat, React
Purpose: Build robust blockchain applications with comprehensive testing and deployment
</dartinbot-detect>

## Tech Stack Configuration
<dartinbot-brain 
    specialty="blockchain-development"
    model="gpt-4"
    focus="smart-contracts,dapps,web3,defi"
    expertise-level="advanced">

### Smart Contract Development
- **Framework**: Hardhat with TypeScript support
- **Language**: Solidity ^0.8.19
- **Testing**: Waffle, Chai, Ethers.js
- **Security**: Slither, MythX integration
- **Gas Optimization**: Automated optimization checks

### Frontend Integration
- **Framework**: React with TypeScript
- **Web3 Library**: Ethers.js v6
- **Wallet Integration**: MetaMask, WalletConnect
- **UI Components**: Web3Modal, Chakra UI
- **State Management**: Zustand with persistence

### Development Environment
- **Local Blockchain**: Hardhat Network
- **Testnet**: Sepolia, Goerli
- **Mainnet**: Ethereum, Polygon
- **Deployment**: Hardhat Deploy scripts
- **Verification**: Etherscan integration

## Smart Contract Architecture

### Core Contract Structure
```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/Pausable.sol";

contract DAppCore is ReentrancyGuard, Ownable, Pausable {
    // State variables
    mapping(address => uint256) public balances;
    
    // Events
    event Deposit(address indexed user, uint256 amount);
    event Withdrawal(address indexed user, uint256 amount);
    
    // Modifiers
    modifier validAmount(uint256 _amount) {
        require(_amount > 0, "Amount must be greater than zero");
        _;
    }
    
    // Functions with security patterns
    function deposit() external payable validAmount(msg.value) whenNotPaused nonReentrant {
        balances[msg.sender] += msg.value;
        emit Deposit(msg.sender, msg.value);
    }
    
    function withdraw(uint256 _amount) external validAmount(_amount) whenNotPaused nonReentrant {
        require(balances[msg.sender] >= _amount, "Insufficient balance");
        
        balances[msg.sender] -= _amount;
        
        (bool success, ) = payable(msg.sender).call{value: _amount}("");
        require(success, "Transfer failed");
        
        emit Withdrawal(msg.sender, _amount);
    }
}
```

## Project Structure

### Smart Contracts Directory
```
contracts/
├── core/
│   ├── DAppCore.sol
│   ├── TokenManager.sol
│   └── GovernanceToken.sol
├── interfaces/
│   ├── IDAppCore.sol
│   └── ITokenManager.sol
├── libraries/
│   ├── SafeMath.sol
│   └── AddressUtils.sol
├── mocks/
│   └── MockERC20.sol
└── upgrades/
    └── DAppCoreV2.sol
```

### Frontend Structure
```
frontend/
├── src/
│   ├── components/
│   │   ├── WalletConnect.tsx
│   │   ├── ContractInteraction.tsx
│   │   └── TransactionHistory.tsx
│   ├── hooks/
│   │   ├── useContract.ts
│   │   ├── useWallet.ts
│   │   └── useBlockchain.ts
│   ├── utils/
│   │   ├── web3.ts
│   │   ├── contracts.ts
│   │   └── formatters.ts
│   └── store/
│       └── walletStore.ts
└── public/
    └── contracts/
        └── deployments.json
```

## Configuration Files

### Hardhat Configuration
<dartinbot-config type="hardhat.config.ts">
```typescript
import { HardhatUserConfig } from "hardhat/config";
import "@nomicfoundation/hardhat-toolbox";
import "hardhat-deploy";
import "hardhat-gas-reporter";
import "solidity-coverage";

const config: HardhatUserConfig = {
  solidity: {
    version: "0.8.19",
    settings: {
      optimizer: {
        enabled: true,
        runs: 200,
      },
    },
  },
  networks: {
    hardhat: {
      chainId: 31337,
    },
    sepolia: {
      url: process.env.SEPOLIA_URL || "",
      accounts: process.env.PRIVATE_KEY ? [process.env.PRIVATE_KEY] : [],
    },
    mainnet: {
      url: process.env.MAINNET_URL || "",
      accounts: process.env.PRIVATE_KEY ? [process.env.PRIVATE_KEY] : [],
    },
  },
  gasReporter: {
    enabled: process.env.REPORT_GAS !== undefined,
    currency: "USD",
  },
  etherscan: {
    apiKey: process.env.ETHERSCAN_API_KEY,
  },
};

export default config;
```
</dartinbot-config>

### Package.json Dependencies
<dartinbot-config type="package.json">
```json
{
  "name": "dapp-project",
  "scripts": {
    "compile": "hardhat compile",
    "test": "hardhat test",
    "test:coverage": "hardhat coverage",
    "deploy:local": "hardhat deploy --network hardhat",
    "deploy:sepolia": "hardhat deploy --network sepolia",
    "verify": "hardhat etherscan-verify --network sepolia",
    "frontend": "cd frontend && npm start"
  },
  "devDependencies": {
    "@nomicfoundation/hardhat-toolbox": "^3.0.0",
    "@openzeppelin/contracts": "^4.9.0",
    "hardhat": "^2.17.0",
    "hardhat-deploy": "^0.11.0",
    "hardhat-gas-reporter": "^1.0.9",
    "solidity-coverage": "^0.8.0",
    "typescript": "^5.0.0"
  }
}
```
</dartinbot-config>

## Testing Framework

### Smart Contract Tests
<dartinbot-test type="unit-test">
```typescript
import { expect } from "chai";
import { ethers } from "hardhat";
import { DAppCore } from "../typechain-types";

describe("DAppCore", function () {
  let dappCore: DAppCore;
  let owner: any;
  let user1: any;
  let user2: any;

  beforeEach(async function () {
    [owner, user1, user2] = await ethers.getSigners();
    
    const DAppCoreFactory = await ethers.getContractFactory("DAppCore");
    dappCore = await DAppCoreFactory.deploy();
    await dappCore.deployed();
  });

  describe("Deposit", function () {
    it("Should accept deposits", async function () {
      const depositAmount = ethers.utils.parseEther("1.0");
      
      await expect(dappCore.connect(user1).deposit({ value: depositAmount }))
        .to.emit(dappCore, "Deposit")
        .withArgs(user1.address, depositAmount);
      
      expect(await dappCore.balances(user1.address)).to.equal(depositAmount);
    });

    it("Should reject zero deposits", async function () {
      await expect(dappCore.connect(user1).deposit({ value: 0 }))
        .to.be.revertedWith("Amount must be greater than zero");
    });
  });

  describe("Withdrawal", function () {
    beforeEach(async function () {
      const depositAmount = ethers.utils.parseEther("2.0");
      await dappCore.connect(user1).deposit({ value: depositAmount });
    });

    it("Should allow withdrawals", async function () {
      const withdrawAmount = ethers.utils.parseEther("1.0");
      
      await expect(dappCore.connect(user1).withdraw(withdrawAmount))
        .to.emit(dappCore, "Withdrawal")
        .withArgs(user1.address, withdrawAmount);
    });

    it("Should reject withdrawals exceeding balance", async function () {
      const withdrawAmount = ethers.utils.parseEther("3.0");
      
      await expect(dappCore.connect(user1).withdraw(withdrawAmount))
        .to.be.revertedWith("Insufficient balance");
    });
  });
});
```
</dartinbot-test>

## Security Patterns

### Reentrancy Protection
<dartinbot-security pattern="reentrancy-guard">
- Use OpenZeppelin's ReentrancyGuard
- Follow checks-effects-interactions pattern
- Update state before external calls
- Use nonReentrant modifier on external functions
</dartinbot-security>

### Access Control
<dartinbot-security pattern="access-control">
- Implement role-based access control
- Use OpenZeppelin's AccessControl
- Validate function caller permissions
- Emit events for administrative actions
</dartinbot-security>

### Integer Overflow Protection
<dartinbot-security pattern="overflow-protection">
- Use Solidity ^0.8.0 for automatic overflow checks
- Validate input parameters
- Use SafeMath for additional operations if needed
- Check for division by zero
</dartinbot-security>

## Deployment Scripts

### Deployment Configuration
<dartinbot-deployment type="deployment-script">
```typescript
import { HardhatRuntimeEnvironment } from "hardhat/types";
import { DeployFunction } from "hardhat-deploy/types";

const deployDAppCore: DeployFunction = async function (hre: HardhatRuntimeEnvironment) {
  const { deployments, getNamedAccounts } = hre;
  const { deploy } = deployments;

  const { deployer } = await getNamedAccounts();

  const dappCore = await deploy("DAppCore", {
    from: deployer,
    args: [],
    log: true,
    waitConfirmations: hre.network.name === "hardhat" ? 1 : 6,
  });

  if (hre.network.name !== "hardhat") {
    await hre.run("etherscan-verify", {
      address: dappCore.address,
    });
  }
};

export default deployDAppCore;
deployDAppCore.tags = ["DAppCore"];
```
</dartinbot-deployment>

## Frontend Integration

### Web3 Hook
<dartinbot-frontend type="react-hook">
```typescript
import { useState, useEffect } from 'react';
import { ethers } from 'ethers';
import { DAppCore__factory } from '../typechain-types';

export const useContract = (contractAddress: string) => {
  const [contract, setContract] = useState<any>(null);
  const [provider, setProvider] = useState<ethers.providers.Web3Provider | null>(null);

  useEffect(() => {
    const initializeContract = async () => {
      if (window.ethereum) {
        const web3Provider = new ethers.providers.Web3Provider(window.ethereum);
        const signer = web3Provider.getSigner();
        
        const contractInstance = DAppCore__factory.connect(contractAddress, signer);
        
        setProvider(web3Provider);
        setContract(contractInstance);
      }
    };

    initializeContract();
  }, [contractAddress]);

  return { contract, provider };
};
```
</dartinbot-frontend>

## Performance Optimization

### Gas Optimization
<dartinbot-optimization type="gas-optimization">
- Use `uint256` instead of smaller integers
- Pack struct variables efficiently
- Use `calldata` for read-only function parameters
- Minimize storage operations
- Use events for cheaper data storage
- Optimize loop operations
- Consider using libraries for complex calculations
</dartinbot-optimization>

### Frontend Optimization
<dartinbot-optimization type="frontend-optimization">
- Implement connection pooling for RPC calls
- Cache contract instances and ABIs
- Use event filters for efficient data fetching
- Implement optimistic updates for better UX
- Use Web3Modal for wallet management
- Implement transaction queueing
</dartinbot-optimization>

## Error Handling

### Smart Contract Error Handling
<dartinbot-error-handling type="solidity">
```solidity
// Custom errors (more gas efficient)
error InsufficientBalance(uint256 available, uint256 required);
error InvalidAmount();
error TransferFailed();

// Usage in functions
function withdraw(uint256 _amount) external {
    if (_amount == 0) revert InvalidAmount();
    if (balances[msg.sender] < _amount) {
        revert InsufficientBalance(balances[msg.sender], _amount);
    }
    
    balances[msg.sender] -= _amount;
    
    (bool success, ) = payable(msg.sender).call{value: _amount}("");
    if (!success) revert TransferFailed();
}
```
</dartinbot-error-handling>

### Frontend Error Handling
<dartinbot-error-handling type="typescript">
```typescript
export const handleContractError = (error: any) => {
  if (error.code === 4001) {
    return "Transaction rejected by user";
  } else if (error.code === -32603) {
    return "Internal JSON-RPC error";
  } else if (error.message?.includes("insufficient funds")) {
    return "Insufficient funds for transaction";
  } else if (error.message?.includes("user rejected")) {
    return "Transaction cancelled by user";
  }
  
  return error.message || "Unknown error occurred";
};
```
</dartinbot-error-handling>

## CI/CD Pipeline

### GitHub Actions Workflow
<dartinbot-cicd type="github-actions">
```yaml
name: Smart Contract CI/CD

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Setup Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '18'
          
      - name: Install dependencies
        run: npm install
        
      - name: Compile contracts
        run: npx hardhat compile
        
      - name: Run tests
        run: npx hardhat test
        
      - name: Generate coverage
        run: npx hardhat coverage
        
      - name: Security analysis
        run: |
          npm install -g slither-analyzer
          slither contracts/

  deploy-testnet:
    needs: test
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/develop'
    steps:
      - uses: actions/checkout@v3
      
      - name: Deploy to Sepolia
        run: npx hardhat deploy --network sepolia
        env:
          SEPOLIA_URL: ${{ secrets.SEPOLIA_URL }}
          PRIVATE_KEY: ${{ secrets.PRIVATE_KEY }}
          
      - name: Verify contracts
        run: npx hardhat etherscan-verify --network sepolia
        env:
          ETHERSCAN_API_KEY: ${{ secrets.ETHERSCAN_API_KEY }}
```
</dartinbot-cicd>

## Documentation

### API Documentation
<dartinbot-docs type="api-documentation">
Generate comprehensive API documentation using:
- Solidity NatSpec comments for contracts
- TypeDoc for TypeScript frontend code
- Hardhat docgen for automatic documentation
- README with setup and usage instructions
- Architecture decision records (ADRs)
</dartinbot-docs>

## Monitoring and Analytics

### Contract Monitoring
<dartinbot-monitoring type="contract-monitoring">
- Transaction monitoring with Etherscan API
- Gas usage tracking and optimization alerts
- Contract event logging and analysis
- Error rate monitoring and alerting
- Performance metrics dashboard
- Security incident response procedures
</dartinbot-monitoring>

## Next Steps
<dartinbot-auto-improve>
1. **Enhanced Security**: Add multi-signature wallet integration
2. **Scalability**: Implement Layer 2 solutions (Polygon, Arbitrum)
3. **Governance**: Add DAO governance mechanisms
4. **Interoperability**: Cross-chain bridge integration
5. **Analytics**: Advanced on-chain analytics dashboard
6. **Mobile**: React Native mobile app development
7. **Testing**: Property-based testing with Echidna
8. **Upgradability**: Implement proxy patterns for contract upgrades
</dartinbot-auto-improve>

## Troubleshooting Guide
<dartinbot-troubleshooting>
**Common Issues:**
1. **Gas estimation failures**: Check contract state and input validation
2. **MetaMask connection issues**: Verify network configuration and permissions
3. **Transaction reverts**: Review error messages and contract requirements
4. **Deployment failures**: Validate constructor parameters and network settings
5. **Frontend state issues**: Check provider connection and contract addresses

**Debug Commands:**
- `npx hardhat console --network localhost`
- `npx hardhat test --verbose`
- `npx hardhat coverage`
- `npx hardhat size-contracts`
</dartinbot-troubleshooting>

</dartinbot-template>
