using Microsoft.Extensions.Logging;

namespace Example.Project;

/// <summary>
/// Coordinates a focused application use case.
/// </summary>
public sealed class ExampleService
{
    private readonly IExampleGateway _gateway;
    private readonly ILogger<ExampleService> _logger;

    /// <summary>
    /// Initializes a new instance of the <see cref="ExampleService"/> class.
    /// </summary>
    public ExampleService(
        IExampleGateway gateway,
        ILogger<ExampleService> logger)
    {
        ArgumentNullException.ThrowIfNull(gateway);
        ArgumentNullException.ThrowIfNull(logger);

        _gateway = gateway;
        _logger = logger;
    }

    /// <summary>
    /// Retrieves an item after validating the application input.
    /// </summary>
    public async Task<ExampleItem?> GetAsync(
        string identifier,
        CancellationToken cancellationToken)
    {
        if (string.IsNullOrWhiteSpace(identifier))
        {
            throw new ArgumentException(
                "The identifier cannot be empty or whitespace.",
                nameof(identifier));
        }

        _logger.LogDebug(
            "Retrieving example item {Identifier}",
            identifier);

        ExampleItem? item = await _gateway.GetByIdAsync(
            identifier,
            cancellationToken);

        if (item is null)
        {
            _logger.LogInformation(
                "Example item {Identifier} was not found",
                identifier);
        }

        return item;
    }
}
