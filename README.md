# proto-dotnet-plugin

A [proto](https://moonrepo.dev/proto) TOML plugin for managing [.NET SDK](https://dotnet.microsoft.com/) versions.

## Installation

```bash
proto plugin add dotnet "https://raw.githubusercontent.com/RemiKalbe/proto-dotnet-plugin/main/plugin.toml"
```

Or add it manually to `.prototools`:

```toml
[plugins]
dotnet = "https://raw.githubusercontent.com/RemiKalbe/proto-dotnet-plugin/main/plugin.toml"
```

## Usage

```bash
# Install latest .NET SDK
proto install dotnet

# Install a specific version
proto install dotnet 9.0.205

# Install .NET 8 LTS
proto install dotnet 8.0.418

# Run dotnet with a specific version
proto run dotnet 9.0.205 -- --version

# Pin a version in current project
proto pin dotnet 9.0.205
```

## Version detection

The plugin detects versions from `global.json` files, matching the standard .NET convention.

## Supported platforms

| Platform | Architectures |
|----------|--------------|
| macOS    | arm64, x64   |
| Linux    | arm64, x64   |
| Windows  | arm64, x64   |

## How it works

Downloads pre-built SDK archives directly from Microsoft's official CDN (`builds.dotnet.microsoft.com`). Versions are resolved from git tags on the [dotnet/sdk](https://github.com/dotnet/sdk) repository, filtering to stable releases only.

## License

MIT
