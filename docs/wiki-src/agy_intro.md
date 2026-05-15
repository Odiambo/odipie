# Understanding Antigravity (AGY) and the Future of Agentic Coding

## Introduction to Antigravity (AGY)

**Antigravity (AGY)** is Google's agentic development platform for software engineering. It acts as a mission-control layer for AI agents that can plan, code, run tools, use the browser, and produce artifacts that explain what they did. Instead of only accelerating line-by-line coding, Antigravity shifts more of the workflow toward task-oriented, agent-assisted development.

At its core, Antigravity uses Gemini models and an agent-first workflow that spans the editor, terminal, and browser. That lets it reason across larger contexts, execute multi-step tasks, and verify outcomes with artifacts such as task lists, implementation plans, walkthroughs, screenshots, and browser recordings.

### Key Capabilities
*   **Autonomous Execution**: AGY agents can take a high-level objective (e.g., "Refactor the authentication module") and break it down into a concrete plan, execute the necessary code changes, and verify the results.
*   **Artifact Generation**: To maintain transparency and trust, AGY generates "Artifacts"—structured documents like implementation plans, task lists, and walkthroughs. These allow developers to review the agent's logic and progress without parsing raw logs.
*   **Multi-Surface Workflow**: Antigravity combines an AI-powered editor, Agent Manager, and browser agent so work can continue across multiple workspaces and surfaces.
*   **Tool and Browser Access**: Unlike simple autocomplete tools, AGY can work across the codebase, terminal, browser, and connected services, allowing it to build, test, research, and debug end-to-end tasks.

---

## The Engine: Model Context Protocol (MCP)

A critical component enabling Antigravity's capabilities is the **Model Context Protocol (MCP)**. Think of MCP as a "USB-C port for AI applications."

Traditionally, Large Language Models (LLMs) are isolated from the real world. MCP solves this by providing a standardized way for AI systems to connect to external data sources and tools. In Antigravity, MCP is how the editor can securely pull in live context and invoke approved actions from connected services.

### How MCP Works
*   **Client-Server Architecture**: Antigravity acts as the host and connects to MCP servers that expose resources and tools.
*   **Standardized Access**: MCP servers can provide live context such as schemas, logs, tickets, documents, and API-backed actions in a uniform format.
*   **Built-In and Custom Connections**: Antigravity supports a built-in MCP Store and also allows custom MCP server configuration for internal tools and private systems.

---

## Application Capabilities

Antigravity is designed to handle a wide spectrum of development tasks:

1.  **Greenfield Development**: Building full-stack web applications from scratch, including frontend UI, backend logic, and database schema design.
2.  **Legacy Modernization**: Analyzing complex, undocumented codebases to refactor technical debt, upgrade dependencies, or migrate to modern frameworks.
3.  **Automated Workflows**: Creating and executing scripts for DevOps tasks, data processing pipelines, and system maintenance.
4.  **Debugging & Verification**: Autonomously investigating bugs by adding logs, creating reproduction scripts, running test suites, and visually verifying UI fixes in a browser.

---

## Installation Guide

Antigravity is available for Windows, macOS, and supported Linux distributions.

### Prerequisites
*   **Google Chrome**: Required for browser integration features.
*   **Google Account**: Antigravity is currently available for personal Google accounts in approved geographies. A personal Gmail account is recommended, and Workspace accounts may not authenticate reliably.
*   **Age and Region Eligibility**: Antigravity is currently unavailable to under-18 users and is only supported in approved countries and territories.

### Platform Support Snapshot
*   **Windows**: Windows 10 (64-bit).
*   **macOS**: macOS 12 Monterey or newer with Apple security update support. Intel x86 Macs are not supported.
*   **Linux**: Supported on distributions that meet the published runtime requirements, including `glibc >= 2.28` and `glibcxx >= 3.4.25`.

### Windows Installation
1.  **Download**: Visit the [official Antigravity download page](https://antigravity.google/download) and download the Windows installer (`.exe`).
2.  **Install**: Run the installer. Follow the on-screen prompts.
3.  **Path Setup**: Ensure you check the option to **"Add `agy` to PATH"** during installation. This enables you to launch Antigravity from the command line using `agy .`.
4.  **Setup**: Launch the application. You will be prompted to install the Antigravity Chrome Extension. Click "Setup" and follow the instructions to add it to Chrome.
5.  **Login**: Sign in with your Google account.

### Linux Installation
1.  **Download**: Download the Linux client from the [official Antigravity download page](https://antigravity.google/download).
2.  **Install**: Run the following command in your terminal (replace `filename` with the actual downloaded file):
    ```bash
    sudo dpkg -i antigravity_client_filename.deb
    ```
    If there are missing dependencies, run:
    ```bash
    sudo apt-get install -f
    ```
3.  **Path Setup**: Verify that `agy` is in your path. You may need to restart your terminal session.
4.  **Setup**: Launch `agy` from the terminal. Follow the prompts to install the Chrome Extension and sign in.

### macOS Installation
1.  **Download**: Visit the [official Antigravity download page](https://antigravity.google/download) and download the macOS disk image (`.dmg`).
2.  **Install**: Open the `.dmg` file and drag the **Antigravity** app into your `/Applications` folder.
3.  **Path Setup**: Open a terminal and verify the CLI is accessible:
    ```bash
    agy --version
    ```
    If the command is not found, add the binary to your shell profile manually:
    ```bash
    echo 'export PATH="/Applications/Antigravity.app/Contents/MacOS:$PATH"' >> ~/.zshrc
    source ~/.zshrc
    ```
4.  **Gatekeeper**: On first launch, macOS may block the app since it is downloaded from the internet. Go to **System Settings → Privacy & Security** and click **"Open Anyway"** next to the Antigravity entry.
5.  **Setup**: Launch the application or run `agy .` from your project directory. Follow the prompts to install the Antigravity Chrome Extension and connect it to Chrome.
6.  **Login**: Sign in with your Google account.

> **Note**: Apple Silicon (M-series) Macs are supported natively. Rosetta 2 is not required.

---

## Troubleshooting: macOS Gatekeeper & Security Issues

For macOS, **Gatekeeper** and **System Integrity Protection (SIP)** may prevent Antigravity from launching or accessing the browser.

### Symptoms
*   "Antigravity cannot be opened because it is from an unidentified developer."
*   Chrome instance fails to connect to the AGY host process.
*   `agy` command not found after installation.

### Resolution Steps

**1. Allow the App via System Settings**
```
System Settings → Privacy & Security → scroll to "Security" → Open Anyway
```

**2. Remove Quarantine Attribute (Advanced)**
If the app remains blocked, clear the quarantine flag via terminal:
```bash
xattr -dr com.apple.quarantine /Applications/Antigravity.app
```

**3. CLI Not Found**
If `agy` is not found after installation, ensure the binary path is in your `$PATH` (see step 3 of the installation guide above). Run `source ~/.zshrc` (or `~/.bash_profile` for Bash users) after editing.

---

## Troubleshooting: Ubuntu AppArmor Issues

On Ubuntu systems, **AppArmor** (a security module) may occasionally block Antigravity or its Chrome integration from launching or accessing necessary resources.

### Symptoms
*   Antigravity fails to launch.
*   Chrome instance fails to start or connect.
*   System logs (`dmesg` or `/var/log/syslog`) show `apparmor="DENIED"` messages related to `agy` or `chrome`.

### Resolution Steps

**1. Check AppArmor Status**
First, verify if AppArmor is the culprit by checking the logs:
```bash
sudo grep "DENIED" /var/log/syslog | grep agy
```

**2. Switch Profile to Complain Mode**
The safest immediate fix is to switch the relevant AppArmor profile to "complain mode." This allows the application to run while logging what *would* have been blocked, rather than enforcing the block.

Find the profile name (usually related to the binary path, e.g., `opt.google.antigravity.agy`):
```bash
# List all profiles
sudo apparmor_status

# Switch to complain mode (replace with actual profile name)
sudo aa-complain /etc/apparmor.d/opt.google.antigravity.agy
```

**3. Reload AppArmor**
After changing the mode, reload the AppArmor profiles:
```bash
sudo systemctl reload apparmor
```

**4. Permanent Fix (Advanced)**
If you need to keep Enforce mode active, you can update the profile to allow the specific actions being blocked:
1.  Run `sudo aa-logprof`.
2.  Follow the interactive prompts to "Allow" the legitimate actions requested by Antigravity.
3.  Switch back to enforce mode: `sudo aa-enforce /etc/apparmor.d/opt.google.antigravity.agy`.

> **Note**: In rare cases on newer Ubuntu versions (23.10+), user namespace restrictions may also interfere. Ensure your system is up to date and check the official Antigravity support forums for specific kernel parameter workarounds if issues persist.

---

## FAQ 

### What is Google Antigravity?
Google Antigravity is Google's agentic development platform. It combines an AI-powered editor, Agent Manager, and browser agent so developers can delegate larger software tasks to autonomous agents.

### What does AGY mean?
AGY is a common shorthand for Antigravity. In practice, AGY refers to the Antigravity product, its CLI, and its agent workflow.

### What can Antigravity do?
Antigravity can plan tasks, edit code, run terminal commands, browse the web, connect to tools through MCP, and generate artifacts such as task lists, implementation plans, walkthroughs, screenshots, and browser recordings.

### Does Antigravity require a Google account?
Yes. Google Antigravity currently requires a personal Google account in an approved geography for standard access. A personal Gmail account is the safest choice during the current preview period.

### Can I use a Google Workspace account with Antigravity?
Sometimes, but Workspace account authentication is not the recommended path. Google currently advises trying an `@gmail.com` account if a Workspace account has sign-in issues.

### Does Antigravity support MCP?
Yes. Antigravity supports the Model Context Protocol (MCP), including built-in MCP Store integrations and custom MCP server configuration for internal tools and external services.

### Does Antigravity support Windows, macOS, and Linux?
Yes. Antigravity supports Windows 10 64-bit, modern supported macOS releases, and supported Linux distributions that meet Google's published runtime requirements.

### Does Antigravity support worktrees?
Not currently. Google's FAQ states that Antigravity does not currently support worktrees.

### How does Antigravity update?
The official docs say the application prompts when updates are available. If you installed Antigravity through another package management flow, use that same installation path to apply updates and then verify with `agy --version`.

### Is Antigravity only a code completion tool?
No. Antigravity includes inline AI assistance, but its main value is orchestrating task-oriented agents that can work across the editor, terminal, browser, and connected systems.

---

# Antigravity Update Workflow

## Overview of the current update process

Updates are primarily app-driven rather than a hidden agent workflow that always opens a background terminal.

The exact update path depends on how Antigravity was installed on your machine. A safe general workflow is:

1. **Watch for the in-app update prompt**

2. **Apply the recommended update or restart action**

3. **If you installed through a package manager, update through that same package manager**

4. **Verify the installed version**
    ```bash
    agy --version
    ```

5. **Confirm the binary path if the version does not match your expectation**

6. **Restart Antigravity if required**

## macOS Update Workflow

On macOS, the same rule applies: prefer the in-app update prompt when available. If you originally installed Antigravity through another package management flow, use that same flow to update it.

1. **Accept the in-app update prompt if one appears**

2. **If you used Homebrew, update through Homebrew**

3. **Verify the updated version**
    ```bash
    agy --version
    ```

4. **If needed, confirm which binary your shell is using**
