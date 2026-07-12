namespace Example.Project;

/// <summary>
/// Defines a meaningful external or behavioral boundary.
/// </summary>
/// <remarks>
/// Do not create an interface merely to mirror every method of a concrete class.
/// Use an interface when multiple implementations, an external boundary, or a
/// stable consumer contract provides real value.
/// </remarks>
public interface IExampleGateway
{
    /// <summary>
    /// Retrieves an item by its stable identifier.
    /// </summary>
    /// <param name="identifier">The non-empty identifier.</param>
    /// <param name="cancellationToken">Cancels the operation.</param>
    /// <returns>The item when found; otherwise, <see langword="null"/>.</returns>
    Task<ExampleItem?> GetByIdAsync(
        string identifier,
        CancellationToken cancellationToken);
}

/// <summary>
/// Represents an immutable item returned by the gateway.
/// </summary>
/// <param name="Identifier">The stable identifier.</param>
/// <param name="DisplayName">The display name.</param>
public sealed record ExampleItem(
    string Identifier,
    string DisplayName);
