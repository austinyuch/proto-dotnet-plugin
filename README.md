# proto-dotnet-plugin

A [proto](https://moonrepo.dev/proto) TOML plugin for managing [.NET SDK](https://dotnet.microsoft.com/) versions.

## Maintained fork and installation

This fork is maintained by austinyuch. Do not consume `main` or automatically merge upstream.
Requires Python 3.11+ and proto installed at `~/.proto/bin/proto`.

1. Clone this fork and check out a reviewed full commit SHA.
2. Review `plugin.toml` and `scripts/configure_proto.py` before execution.
3. Run the wrapper with that same full SHA:

```bash
python3 scripts/configure_proto.py <reviewed-40-character-commit-sha>
python3 scripts/configure_proto.py <reviewed-40-character-commit-sha> --apply
```

The default is a dry run. The wrapper verifies a hardcoded SHA-256 of the reviewed
plugin, backs up `~/.prototools`, and uses `proto plugin add --to user` to configure
an immutable raw GitHub URL under `[tools.dotnet]`. It does not install an SDK.
See [MAINTENANCE.md](MAINTENANCE.md) for update and rollback instructions.

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
