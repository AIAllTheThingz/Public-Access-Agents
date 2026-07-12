namespace Example.Project;

/// <summary>
/// Represents a cohesive domain or application concept.
/// </summary>
public sealed class ExampleComponent
{
    private readonly TimeProvider _timeProvider;

    /// <summary>
    /// Initializes a new instance of the <see cref="ExampleComponent"/> class.
    /// </summary>
    /// <param name="timeProvider">Provides testable access to the current time.</param>
    public ExampleComponent(TimeProvider timeProvider)
    {
        ArgumentNullException.ThrowIfNull(timeProvider);
        _timeProvider = timeProvider;
    }

    /// <summary>
    /// Creates a result for the supplied identifier.
    /// </summary>
    /// <param name="identifier">The non-empty stable identifier.</param>
    /// <returns>A structured result containing the identifier and UTC timestamp.</returns>
    /// <exception cref="ArgumentException">
    /// Thrown when <paramref name="identifier"/> is empty or whitespace.
    /// </exception>
    public ExampleResult Create(string identifier)
    {
        if (string.IsNullOrWhiteSpace(identifier))
        {
            throw new ArgumentException(
                "The identifier cannot be empty or whitespace.",
                nameof(identifier));
        }

        return new ExampleResult(
            identifier,
            _timeProvider.GetUtcNow());
    }
}

/// <summary>
/// Represents the immutable output of <see cref="ExampleComponent"/>.
/// </summary>
/// <param name="Identifier">The stable identifier.</param>
/// <param name="CreatedAtUtc">The UTC creation time.</param>
public sealed record ExampleResult(
    string Identifier,
    DateTimeOffset CreatedAtUtc);
