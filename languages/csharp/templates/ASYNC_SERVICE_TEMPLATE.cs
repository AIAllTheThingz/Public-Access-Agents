using System;
using System.Threading;
using System.Threading.Tasks;

namespace Example.CSharp;

/// <summary>
/// Defines the controlled asynchronous boundary consumed by <see cref="SampleService"/>.
/// </summary>
public interface ISampleClient
{
    /// <summary>
    /// Retrieves a value for a validated identifier.
    /// </summary>
    /// <param name="identifier">The nonempty identifier to retrieve.</param>
    /// <param name="cancellationToken">Signals that the caller no longer needs the operation.</param>
    /// <returns>The retrieved value, or <see langword="null"/> when it does not exist.</returns>
    Task<string?> GetValueAsync(string identifier, CancellationToken cancellationToken);
}

/// <summary>
/// Demonstrates explicit validation and cancellation propagation around an asynchronous dependency.
/// </summary>
public sealed class SampleService
{
    private readonly ISampleClient _client;

    /// <summary>
    /// Initializes a new instance with its required borrowed dependency.
    /// </summary>
    /// <param name="client">The client whose lifetime is owned by the caller or dependency container.</param>
    public SampleService(ISampleClient client)
    {
        ArgumentNullException.ThrowIfNull(client);
        _client = client;
    }

    /// <summary>
    /// Retrieves a value without hiding cancellation or missing-result behavior.
    /// </summary>
    /// <param name="identifier">The nonempty identifier to retrieve.</param>
    /// <param name="cancellationToken">Signals that the caller no longer needs the operation.</param>
    /// <returns>A structured result that distinguishes found and missing values.</returns>
    public async Task<SampleResult> ExecuteAsync(
        string identifier,
        CancellationToken cancellationToken)
    {
        ArgumentException.ThrowIfNullOrWhiteSpace(identifier);
        cancellationToken.ThrowIfCancellationRequested();

        string? value = await _client
            .GetValueAsync(identifier, cancellationToken)
            .ConfigureAwait(false);

        return value is null
            ? SampleResult.CreateNotFound(identifier)
            : SampleResult.CreateFound(identifier, value);
    }
}

/// <summary>
/// Represents the explicit outcome of a sample lookup.
/// </summary>
/// <param name="Identifier">The identifier that was queried.</param>
/// <param name="IsFound">Whether a value was found.</param>
/// <param name="Value">The value when found; otherwise <see langword="null"/>.</param>
public sealed record SampleResult(string Identifier, bool IsFound, string? Value)
{
    /// <summary>Creates a successful result.</summary>
    public static SampleResult CreateFound(string identifier, string value) =>
        new(identifier, true, value);

    /// <summary>Creates a missing-value result.</summary>
    public static SampleResult CreateNotFound(string identifier) =>
        new(identifier, false, null);
}
