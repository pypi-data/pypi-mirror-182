import sgqlc.types
# import sgqlc.types.datetime


api_schema_new = sgqlc.types.Schema()



########################################################################
# Scalars and Enumerations
########################################################################
class APTSortColumns(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('ATTACKS', 'DELTA', 'MENTIONS', 'NAME', 'SCORE')


class AccessLevelSorting(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('id', 'name', 'order')


class AccountSorting(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('creator', 'id', 'lastUpdater', 'name', 'platformId', 'systemRegistrationDate', 'systemUpdateDate', 'url')


class AggregationFunction(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('daily', 'monthly', 'weekly')


class AggregationType(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('HALF_YEAR', 'MONTH', 'QUARTER', 'WEEK', 'YEAR')


class AllowedFunctionsEnum(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('Administration', 'EditCrawlers', 'EditDocumentFeeds', 'EditExport', 'EditIssues', 'EditKBAndDocuments', 'EditReferenceInfo', 'EditResearchMaps', 'EditStream', 'EditTasks', 'EditTransformations', 'ExportKBAndDocuments', 'ReadCrawlers', 'ReadDocumentFeeds', 'ReadExport', 'ReadIssues', 'ReadKBAndDocuments', 'ReadReferenceInfo', 'ReadReportExport', 'ReadResearchMaps', 'ReadStream', 'ReadTasks', 'ReadTransformations', 'RunTransformations')


class AutocompleteConceptDestination(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('markers',)


class AutocompleteDocumentDestination(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('links', 'markers')


Boolean = sgqlc.types.Boolean

class BulkType(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('account', 'concept', 'document', 'issue', 'map', 'platform')


class CWESortColumns(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('NAME',)


class ChartAggregationType(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('count', 'mean', 'median', 'sum')


class ChartRTarget(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('aptGroups', 'documents', 'exploits', 'malwares', 'organizations', 'software', 'vulns')


class ChartTarget(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('document',)


class ChartType(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('bar', 'cloud', 'column', 'indicator', 'line', 'pie')


class CollectionStatus(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('Canceled', 'Error', 'InProgress', 'Success', 'WithMistakes')


class ComponentView(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('keyValue', 'value')


class CompositeConceptTypeSorting(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('id', 'name')


class CompositeConceptTypeWidgetTypeSorting(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('id', 'name', 'order')


class CompositePropertyTypeSorting(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('id', 'name', 'registrationDate')


class CompositePropertyValueTemplateSorting(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('id', 'name', 'registrationDate')


class ConceptLinkDirection(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('from', 'to')


class ConceptLinkTypeSorting(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('conceptType', 'id', 'name')


class ConceptPropertyTypeSorting(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('name', 'registrationDate')


class ConceptPropertyValueTypeSorting(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('dictionary', 'id', 'name', 'regexp', 'valueType')


class ConceptSorting(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('accessLevel', 'countConcepts', 'countConceptsAndDocuments', 'countDocumentFacts', 'countDocumentMentions', 'countEvents', 'countObjects', 'countPotentialDocuments', 'countProperties', 'countResearchMaps', 'countTasks', 'creator', 'id', 'lastUpdater', 'name', 'score', 'systemRegistrationDate', 'systemUpdateDate')


class ConceptTransformConfigSort(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('description', 'id', 'systemRegistrationDate', 'systemUpdateDate')


class ConceptTransformTaskSort(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('config', 'createTime', 'state')


class ConceptTransformTaskState(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('failed', 'ok', 'pending')


class ConceptTypeLinkMetadata(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('creator', 'endDate', 'lastUpdater', 'linkType', 'registrationDate', 'startDate', 'updateDate')


class ConceptTypeMetadata(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('concept', 'conceptType', 'creator', 'endDate', 'lastUpdater', 'markers', 'name', 'notes', 'startDate', 'systemRegistrationDate', 'systemUpdateDate')


class ConceptTypeSorting(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('dictionary', 'id', 'name', 'regexp')


class ConceptUpdate(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('link', 'linkProperty', 'metadata', 'property')


class ConceptVariant(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('event', 'obj')


class ConceptViewColumnType(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('accessLevel', 'conceptType', 'creator', 'id', 'image', 'lastUpdater', 'metrics', 'name', 'systemRegistrationDate', 'systemUpdateDate')


class ConceptViewMetricType(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('countConcepts', 'countConceptsAndDocuments', 'countDocumentFacts', 'countDocumentMentions', 'countEvents', 'countObjects', 'countPotentialDocuments', 'countProperties', 'countResearchMaps', 'countTasks')


class CountryTarget(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('account', 'platform')


class CrawlerSorting(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('avgPerformanceTime', 'id', 'lastCollectionDate', 'projectTitle', 'title')


class CrawlersType(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('EggFileCrawlers', 'SitemapCrawlers')


class CredentialSorting(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('dataType', 'domain', 'id', 'status', 'value')


class CredentialStatus(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('Invalid', 'Valid')


class CredentialType(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('Account', 'Token')


class DashboardPanelType(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('chart', 'concept', 'conceptView', 'document', 'empty', 'task')


class DocumentFeedMode(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('all', 'deleted', 'favorites')


class DocumentFeedSorting(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('creator', 'id', 'lastUpdater', 'name', 'systemRegistrationDate', 'systemUpdateDate')


class DocumentGrouping(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('none', 'story')


class DocumentRecall(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('high', 'low', 'medium', 'none')


class DocumentSorting(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('countChildDocs', 'countConcepts', 'countDisambiguatedEntities', 'countEntities', 'countEvents', 'countLinks', 'countNamedEntities', 'countObjects', 'countResearchMaps', 'countTasks', 'id', 'publicationDate', 'registrationDate', 'score', 'secretLevel', 'text', 'title', 'trustLevel', 'updateDate')


class DocumentSourceType(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('external', 'internal')


class DocumentType(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('image', 'text')


class DocumentUpdate(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('content', 'markup', 'metadata')


class DocumentViewColumnType(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('creator', 'image', 'lastUpdater', 'markers', 'metrics', 'notes', 'publicationAuthor', 'publicationDate', 'registrationDate', 'secretLevel', 'trustLevel', 'updateDate')


class DocumentViewMetricType(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('countChildDocs', 'countConcepts', 'countDisambiguatedEntities', 'countEntities', 'countEvents', 'countLinks', 'countNamedEntities', 'countObjects', 'countResearchMaps', 'countTasks')


class ElementType(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('blackList', 'whiteList')


class EventLevel(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('error', 'info', 'success', 'warning')


class EventTarget(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('api', 'authApi', 'crawlersApi', 'notificationApi', 'talismanConnector', 'talismanTranslator', 'tcontroller', 'tsearch')


class ExplSortColumns(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('CVSS', 'DELTA', 'INTEGRAL', 'MENTIONS', 'NAME', 'PUBLICATION_DATE', 'SCORE')


class ExploitNamesSortColumns(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('NAME',)


class ExportEntityType(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('concept', 'document')


class ExportTaskSort(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('createTime', 'exporter', 'state')


class ExportTaskState(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('failed', 'ok', 'pending')


class ExporterSort(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('id',)


class ExternalSearchJobSorting(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('ID', 'SearchJobId')


class FactStatus(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('approved', 'autoApproved', 'declined', 'hidden', 'new')


Float = sgqlc.types.Float

ID = sgqlc.types.ID

class InformationSourceLoaderActualStatus(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('Daily', 'EveryTwoDays', 'Never', 'Weekly')


class InformationSourceLoaderSorting(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('id', 'status')


class InformationSourceSorting(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('error', 'id', 'job', 'siteName', 'status', 'url')


class Instant(sgqlc.types.Scalar):
    __schema__ = api_schema_new


Int = sgqlc.types.Int

class IssuePriority(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('High', 'Low', 'Medium')


class IssueSorting(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('creator', 'executor', 'id', 'lastUpdater', 'priority', 'registrationDate', 'status', 'topic', 'updateDate')


class IssueStatus(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('canceled', 'closed', 'dataRequested', 'development', 'improvementRequested', 'open', 'reviewRequested')


class ItemsSort(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('timestamp', 'topic')


class JSON(sgqlc.types.Scalar):
    __schema__ = api_schema_new


class JobFinishedSort(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('args', 'collectionStatus', 'crawlerName', 'createdAt', 'createdBy', 'endTime', 'id', 'periodicJobId', 'projectName', 'settings', 'startTime')


class JobPendingSort(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('args', 'crawlerName', 'createdBy', 'id', 'jobPriority', 'periodicJobId', 'projectName', 'queueTime', 'settings')


class JobPriorityType(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('High', 'Highest', 'Low', 'Normal')


class JobRunningSort(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('args', 'crawlerName', 'createdAt', 'createdBy', 'id', 'jobPriority', 'periodicJobId', 'projectName', 'settings', 'startTime')


class JobStatus(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('Finished', 'Pending', 'Running')


class Json(sgqlc.types.Scalar):
    __schema__ = api_schema_new


class KafkaTopicSort(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('activeMessages', 'configDescription', 'configId', 'description', 'duplicateMessages', 'failedMessages', 'okMessages', 'pendingMessages', 'priority', 'systemRegistrationDate', 'systemUpdateDate', 'topic')


class LinkDirection(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('in', 'out', 'undirected')


class Locale(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('eng', 'other', 'ru')


class LogLevel(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('Critical', 'Debug', 'Error', 'Info', 'Trace', 'Warning')


class LogSorting(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('level', 'timestamp')


class Long(sgqlc.types.Scalar):
    __schema__ = api_schema_new


class MalwSortColumns(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('DELTA', 'MENTIONS', 'NAME', 'SCORE')


class MapEdgeType(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('conceptCandidateFactMention', 'conceptFactLink', 'conceptImplicitLink', 'conceptLink', 'conceptLinkCandidateFact', 'conceptMention', 'conceptTypeLink', 'documentLink')


class MapNodeType(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('concept', 'conceptCandidateFact', 'conceptType', 'document')


class MessageSort(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('timestamp',)


class MetricSorting(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('timestamp',)


class NodeType(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('header', 'image', 'json', 'key', 'list', 'other', 'row', 'table', 'text')


class OrgSortColumns(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('ATTACKS', 'DELTA', 'NAME', 'SCORE')


class PeriodicJobSorting(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('changedAt', 'changedBy', 'crawlerId', 'crawlerName', 'createdAt', 'createdBy', 'id', 'name', 'nextScheduleTime', 'priority', 'projectId', 'projectName', 'status')


class PeriodicJobStatus(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('Disabled', 'Enabled')


class PeriodicTaskSorting(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('ChangedAt', 'ChangedBy', 'CreatedAt', 'CreatedBy', 'ID', 'Name', 'NextScheduleTime', 'Status')


class PipelineConfigSort(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('description', 'id', 'systemRegistrationDate', 'systemUpdateDate')


class PlatformSorting(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('creator', 'id', 'lastUpdater', 'name', 'platformType', 'systemRegistrationDate', 'systemUpdateDate', 'url')


class PlatformType(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('blog', 'database', 'fileStorage', 'forum', 'media', 'messenger', 'newsAggregator', 'procurement', 'review', 'socialNetwork')


class ProjectSorting(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('changedAt', 'changedBy', 'createdAt', 'createdBy', 'description', 'id', 'name', 'title')


class PropLinkOrConcept(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('concept', 'link')


class QueryType(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('CustomQuery', 'Table')


class RelatedDocumentSorting(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('publicationDate', 'registrationDate', 'updateDate')


class RequestSorting(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('timestamp',)


class ResearchMapSorting(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('accessLevel', 'conceptAndDocumentLink', 'conceptLink', 'creator', 'documentLink', 'id', 'lastUpdater', 'name', 'systemRegistrationDate', 'systemUpdateDate')


class RunningStatus(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('Disabled', 'Enabled')


class SearchObjectSorting(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('ChangedAt', 'ChangedBy', 'CreatedAt', 'CreatedBy', 'ID', 'Name', 'Target')


class SearchTarget(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('accountFilterSettings', 'conceptTypes', 'concepts', 'crawlers', 'documents', 'external', 'externalImport', 'issueFilterSettings', 'platformFilterSettings')


class SettingsType(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('array', 'boolean', 'float', 'int', 'object', 'string')


class SeverityCategories(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('CRITICAL', 'HIGH', 'LOW', 'MEDIUM', 'NO_DATA')


class SoftVulnSortColumns(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('DELTA', 'MEDIAN', 'NAME', 'TOTAL_VULNS')


class SoftwareNamesSortColumns(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('NAME',)


class SortDirection(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('ascending', 'descending')


class StepStatus(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('Error', 'InProgress', 'Pending', 'Success')


String = sgqlc.types.String

class TaskFinishedSort(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('EndTime', 'ID', 'StartTime')


class TaskPendingSort(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('ID', 'QueueTime')


class TaskRunningSort(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('ID', 'StartTime')


class TaskStatus(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('Finished', 'Pending', 'Running')


class TaskType(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('DB', 'FileRepository', 'HTML', 'Local', 'Report')


class TrustLevel(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('high', 'low', 'medium')


class TypeOfCrawl(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('Actual', 'Retrospective')


class UnixTime(sgqlc.types.Scalar):
    __schema__ = api_schema_new


class Upload(sgqlc.types.Scalar):
    __schema__ = api_schema_new


class UserPipelineTransformSort(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('description', 'id', 'state', 'systemRegistrationDate', 'systemUpdateDate')


class UserServiceState(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('buildFailed', 'imageNotReady', 'noImage', 'ready')


class ValueType(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('Date', 'Double', 'Geo', 'Int', 'Link', 'String', 'StringLocale')


class VersionSorting(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('createdAt', 'id', 'versionName')


class VersionStatus(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('Active', 'Outdated', 'Removed')


class VulnSortColumns(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('CVSS', 'DELTA', 'EXPLOITS', 'INTEGRAL', 'MENTIONS', 'NAME', 'PUBLICATION_DATE', 'SCORE')


class VulnerabilityNamesSortColumns(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('NAME',)


class WidgetTypeTableType(sgqlc.types.Enum):
    __schema__ = api_schema_new
    __choices__ = ('horizontal', 'vertical')



########################################################################
# Input Objects
########################################################################
class AccessLevelCreationInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('name', 'order')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    order = sgqlc.types.Field(Long, graphql_name='order')


class AccessLevelUpdateInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('name',)
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class AccountCreationInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('platform_id', 'name', 'id', 'url', 'country', 'markers', 'params')
    platform_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='platformId')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')
    country = sgqlc.types.Field(String, graphql_name='country')
    markers = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='markers')
    params = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('ParameterInput')), graphql_name='params')


class AccountFilterSettings(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('search_string', 'platform_id', 'id', 'country', 'markers', 'creator', 'last_updater', 'registration_date', 'update_date')
    search_string = sgqlc.types.Field(String, graphql_name='searchString')
    platform_id = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='platformId')
    id = sgqlc.types.Field(ID, graphql_name='id')
    country = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='country')
    markers = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='markers')
    creator = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='creator')
    last_updater = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='lastUpdater')
    registration_date = sgqlc.types.Field('TimestampInterval', graphql_name='registrationDate')
    update_date = sgqlc.types.Field('TimestampInterval', graphql_name='updateDate')


class AccountUpdateInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('account_id', 'platform_id', 'name', 'new_id', 'url', 'country', 'markers', 'params')
    account_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='accountId')
    platform_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='platformId')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    new_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='newId')
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')
    country = sgqlc.types.Field(String, graphql_name='country')
    markers = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='markers')
    params = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ParameterInput'))), graphql_name='params')


class AddDBPeriodicTaskInputInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('title', 'description', 'access_level', 'trust_level', 'topic', 'status', 'cron_expression', 'cron_utcoffset_minutes', 'task_config')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    description = sgqlc.types.Field(String, graphql_name='description')
    access_level = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='accessLevel')
    trust_level = sgqlc.types.Field(sgqlc.types.non_null(TrustLevel), graphql_name='trustLevel')
    topic = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='topic')
    status = sgqlc.types.Field(sgqlc.types.non_null(RunningStatus), graphql_name='status')
    cron_expression = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cronExpression')
    cron_utcoffset_minutes = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='cronUTCOffsetMinutes')
    task_config = sgqlc.types.Field(sgqlc.types.non_null('DBConfigInput'), graphql_name='taskConfig')


class AddFileRepositoryPeriodicTaskInputInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('title', 'description', 'access_level', 'trust_level', 'topic', 'status', 'cron_expression', 'cron_utcoffset_minutes', 'task_config')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    description = sgqlc.types.Field(String, graphql_name='description')
    access_level = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='accessLevel')
    trust_level = sgqlc.types.Field(sgqlc.types.non_null(TrustLevel), graphql_name='trustLevel')
    topic = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='topic')
    status = sgqlc.types.Field(sgqlc.types.non_null(RunningStatus), graphql_name='status')
    cron_expression = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cronExpression')
    cron_utcoffset_minutes = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='cronUTCOffsetMinutes')
    task_config = sgqlc.types.Field(sgqlc.types.non_null('FileRepositoryConfigInput'), graphql_name='taskConfig')


class AddUserGroupMembersParams(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('user_ids', 'group_ids')
    user_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='userIds')
    group_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='groupIds')


class AttachmentInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('url', 'file')
    url = sgqlc.types.Field(String, graphql_name='url')
    file = sgqlc.types.Field(sgqlc.types.non_null(Upload), graphql_name='file')


class AttributeFilterSettings(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('id', 'name')
    id = sgqlc.types.Field(String, graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')


class BulkMarkersInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('ids', 'bulk_type')
    ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids')
    bulk_type = sgqlc.types.Field(sgqlc.types.non_null(BulkType), graphql_name='bulkType')


class BulkMarkersUpdateInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('ids', 'bulk_type', 'markers_to_delete', 'markers_to_add')
    ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids')
    bulk_type = sgqlc.types.Field(sgqlc.types.non_null(BulkType), graphql_name='bulkType')
    markers_to_delete = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='markersToDelete')
    markers_to_add = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='markersToAdd')


class ChartDescriptionInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('chart_type', 'target', 'query', 'aggregation_field', 'aggregation_function', 'output_limiter')
    chart_type = sgqlc.types.Field(sgqlc.types.non_null(ChartType), graphql_name='chartType')
    target = sgqlc.types.Field(sgqlc.types.non_null(ChartTarget), graphql_name='target')
    query = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='query')
    aggregation_field = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='aggregationField')
    aggregation_function = sgqlc.types.Field(AggregationFunction, graphql_name='aggregationFunction')
    output_limiter = sgqlc.types.Field(sgqlc.types.non_null('OutputLimiterInput'), graphql_name='outputLimiter')


class ChartFiltersInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('q', 'soft', 'vuln')
    q = sgqlc.types.Field(String, graphql_name='q')
    soft = sgqlc.types.Field('SoftwareChartFilterSettingsInput', graphql_name='soft')
    vuln = sgqlc.types.Field('VulnChartFilterSettingsInput', graphql_name='vuln')


class ChartOutputLimiterInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('maximum_points', 'minimum_number')
    maximum_points = sgqlc.types.Field(Int, graphql_name='maximumPoints')
    minimum_number = sgqlc.types.Field(Int, graphql_name='minimumNumber')


class ChartPanelInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('chart_type', 'target', 'filters', 'aggregation_function', 'aggregation_field', 'grouping_field', 'grouping_step', 'secondary_grouping_field', 'secondary_grouping_step', 'output_limiter')
    chart_type = sgqlc.types.Field(sgqlc.types.non_null(ChartType), graphql_name='chartType')
    target = sgqlc.types.Field(sgqlc.types.non_null(ChartRTarget), graphql_name='target')
    filters = sgqlc.types.Field(ChartFiltersInput, graphql_name='filters')
    aggregation_function = sgqlc.types.Field(sgqlc.types.non_null(ChartAggregationType), graphql_name='aggregationFunction')
    aggregation_field = sgqlc.types.Field(String, graphql_name='aggregationField')
    grouping_field = sgqlc.types.Field(String, graphql_name='groupingField')
    grouping_step = sgqlc.types.Field(String, graphql_name='groupingStep')
    secondary_grouping_field = sgqlc.types.Field(String, graphql_name='secondaryGroupingField')
    secondary_grouping_step = sgqlc.types.Field(String, graphql_name='secondaryGroupingStep')
    output_limiter = sgqlc.types.Field(ChartOutputLimiterInput, graphql_name='outputLimiter')


class Comment2IssueInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('id_issue', 'comment')
    id_issue = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='idIssue')
    comment = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='comment')


class ComponentValueInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('id', 'value')
    id = sgqlc.types.Field(ID, graphql_name='id')
    value = sgqlc.types.Field(sgqlc.types.non_null('ValueInput'), graphql_name='value')


class CompositeConceptFilterSettings(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('property_filter_settings', 'link_filter_settings', 'concept_variant', 'name', 'exact_name', 'substring', 'access_level_id', 'creator', 'last_updater', 'creation_date', 'update_date', 'markers', 'has_linked_issues', 'composite_concept_type_ids')
    property_filter_settings = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('PropertyFilterSettings')), graphql_name='propertyFilterSettings')
    link_filter_settings = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('LinkFilterSettings')), graphql_name='linkFilterSettings')
    concept_variant = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ConceptVariant)), graphql_name='conceptVariant')
    name = sgqlc.types.Field(String, graphql_name='name')
    exact_name = sgqlc.types.Field(String, graphql_name='exactName')
    substring = sgqlc.types.Field(String, graphql_name='substring')
    access_level_id = sgqlc.types.Field(ID, graphql_name='accessLevelId')
    creator = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='creator')
    last_updater = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='lastUpdater')
    creation_date = sgqlc.types.Field('TimestampInterval', graphql_name='creationDate')
    update_date = sgqlc.types.Field('TimestampInterval', graphql_name='updateDate')
    markers = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='markers')
    has_linked_issues = sgqlc.types.Field(Boolean, graphql_name='hasLinkedIssues')
    composite_concept_type_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='compositeConceptTypeIds')


class CompositeConceptTypeCreationInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('name', 'root_concept_type_id', 'is_default', 'layout', 'has_supporting_documents', 'has_header_information', 'show_in_menu')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    root_concept_type_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='rootConceptTypeId')
    is_default = sgqlc.types.Field(Boolean, graphql_name='isDefault')
    layout = sgqlc.types.Field(String, graphql_name='layout')
    has_supporting_documents = sgqlc.types.Field(Boolean, graphql_name='hasSupportingDocuments')
    has_header_information = sgqlc.types.Field(Boolean, graphql_name='hasHeaderInformation')
    show_in_menu = sgqlc.types.Field(Boolean, graphql_name='showInMenu')


class CompositeConceptTypeFilterSettings(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('name', 'creator', 'last_updater', 'registration_date', 'update_date')
    name = sgqlc.types.Field(String, graphql_name='name')
    creator = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='creator')
    last_updater = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='lastUpdater')
    registration_date = sgqlc.types.Field('TimestampInterval', graphql_name='registrationDate')
    update_date = sgqlc.types.Field('TimestampInterval', graphql_name='updateDate')


class CompositeConceptTypeUpdateInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('id', 'name', 'is_default', 'layout', 'has_supporting_documents', 'has_header_information', 'show_in_menu')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    is_default = sgqlc.types.Field(Boolean, graphql_name='isDefault')
    layout = sgqlc.types.Field(String, graphql_name='layout')
    has_supporting_documents = sgqlc.types.Field(Boolean, graphql_name='hasSupportingDocuments')
    has_header_information = sgqlc.types.Field(Boolean, graphql_name='hasHeaderInformation')
    show_in_menu = sgqlc.types.Field(Boolean, graphql_name='showInMenu')


class CompositeConceptTypeViewInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('concept_type_id', 'composite_concept_type_id')
    concept_type_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='conceptTypeId')
    composite_concept_type_id = sgqlc.types.Field(ID, graphql_name='compositeConceptTypeId')


class CompositeConceptTypeWidgetTypeColumnInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('name', 'is_main_properties', 'list_values', 'concept_link_type_ids_path', 'sort_by_column', 'sort_direction', 'value_info')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    is_main_properties = sgqlc.types.Field(Boolean, graphql_name='isMainProperties')
    list_values = sgqlc.types.Field(Boolean, graphql_name='listValues')
    concept_link_type_ids_path = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('ConceptLinkTypePathInput')), graphql_name='conceptLinkTypeIdsPath')
    sort_by_column = sgqlc.types.Field(Boolean, graphql_name='sortByColumn')
    sort_direction = sgqlc.types.Field(SortDirection, graphql_name='sortDirection')
    value_info = sgqlc.types.Field(sgqlc.types.non_null('CompositeConceptTypeWidgetTypeColumnValueInfoInput'), graphql_name='valueInfo')


class CompositeConceptTypeWidgetTypeColumnValueInfoInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('property_type_id', 'metadata', 'link_property_type_id', 'link_metadata')
    property_type_id = sgqlc.types.Field(ID, graphql_name='propertyTypeId')
    metadata = sgqlc.types.Field(ConceptTypeMetadata, graphql_name='metadata')
    link_property_type_id = sgqlc.types.Field(ID, graphql_name='linkPropertyTypeId')
    link_metadata = sgqlc.types.Field(ConceptTypeLinkMetadata, graphql_name='linkMetadata')


class CompositeConceptTypeWidgetTypeCreationInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('name', 'table_type', 'composite_concept_type_id', 'columns')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    table_type = sgqlc.types.Field(sgqlc.types.non_null(WidgetTypeTableType), graphql_name='tableType')
    composite_concept_type_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='compositeConceptTypeId')
    columns = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CompositeConceptTypeWidgetTypeColumnInput))), graphql_name='columns')


class CompositeConceptTypeWidgetTypeUpdateInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('id', 'name', 'table_type', 'columns')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    table_type = sgqlc.types.Field(sgqlc.types.non_null(WidgetTypeTableType), graphql_name='tableType')
    columns = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CompositeConceptTypeWidgetTypeColumnInput))), graphql_name='columns')


class CompositeConceptTypeWidgetTypeUpdateOrderInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('composite_concept_type_id', 'ids')
    composite_concept_type_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='compositeConceptTypeId')
    ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids')


class CompositePropertyTypeFilterSettings(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('name', 'concept_type_id', 'link_type_id')
    name = sgqlc.types.Field(String, graphql_name='name')
    concept_type_id = sgqlc.types.Field(ID, graphql_name='conceptTypeId')
    link_type_id = sgqlc.types.Field(ID, graphql_name='linkTypeId')


class CompositePropertyValueTemplateCreateInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('id', 'name', 'component_value_types')
    id = sgqlc.types.Field(ID, graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    component_value_types = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('NamedValueType'))), graphql_name='componentValueTypes')


class CompositePropertyValueTemplateFilterSettings(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('name', 'creator', 'last_updater', 'registration_date', 'update_date')
    name = sgqlc.types.Field(String, graphql_name='name')
    creator = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='creator')
    last_updater = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='lastUpdater')
    registration_date = sgqlc.types.Field('TimestampInterval', graphql_name='registrationDate')
    update_date = sgqlc.types.Field('TimestampInterval', graphql_name='updateDate')


class Concept2IssueInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('id_issue', 'concept_ids', 'comment')
    id_issue = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='idIssue')
    concept_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='conceptIds')
    comment = sgqlc.types.Field(String, graphql_name='comment')


class ConceptAddImplicitLinkInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('first_node_id', 'second_node_id')
    first_node_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='firstNodeId')
    second_node_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='secondNodeId')


class ConceptAddInputInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('concept_id', 'x_coordinate', 'y_coordinate', 'group_id')
    concept_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='conceptId')
    x_coordinate = sgqlc.types.Field(Float, graphql_name='xCoordinate')
    y_coordinate = sgqlc.types.Field(Float, graphql_name='yCoordinate')
    group_id = sgqlc.types.Field(ID, graphql_name='groupId')


class ConceptCandidateAddInputInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('document_id', 'group_id')
    document_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='documentId')
    group_id = sgqlc.types.Field(ID, graphql_name='groupId')


class ConceptExtraSettings(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('search_on_map', 'selected_content')
    search_on_map = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='searchOnMap')
    selected_content = sgqlc.types.Field('ResearchMapContentSelectInput', graphql_name='selectedContent')


class ConceptFilterSettings(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('property_filter_settings', 'link_filter_settings', 'concept_type_ids', 'concept_variant', 'name', 'exact_name', 'substring', 'access_level_id', 'creator', 'last_updater', 'creation_date', 'update_date', 'markers', 'has_linked_issues')
    property_filter_settings = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('PropertyFilterSettings')), graphql_name='propertyFilterSettings')
    link_filter_settings = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('LinkFilterSettings')), graphql_name='linkFilterSettings')
    concept_type_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='conceptTypeIds')
    concept_variant = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ConceptVariant)), graphql_name='conceptVariant')
    name = sgqlc.types.Field(String, graphql_name='name')
    exact_name = sgqlc.types.Field(String, graphql_name='exactName')
    substring = sgqlc.types.Field(String, graphql_name='substring')
    access_level_id = sgqlc.types.Field(ID, graphql_name='accessLevelId')
    creator = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='creator')
    last_updater = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='lastUpdater')
    creation_date = sgqlc.types.Field('TimestampInterval', graphql_name='creationDate')
    update_date = sgqlc.types.Field('TimestampInterval', graphql_name='updateDate')
    markers = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='markers')
    has_linked_issues = sgqlc.types.Field(Boolean, graphql_name='hasLinkedIssues')


class ConceptLinkCreationMutationInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('concept_from_id', 'concept_to_id', 'link_type_id', 'notes', 'fact_info', 'start_date', 'end_date', 'access_level_id')
    concept_from_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='conceptFromId')
    concept_to_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='conceptToId')
    link_type_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='linkTypeId')
    notes = sgqlc.types.Field(String, graphql_name='notes')
    fact_info = sgqlc.types.Field('FactInput', graphql_name='factInfo')
    start_date = sgqlc.types.Field('DateTimeValueInput', graphql_name='startDate')
    end_date = sgqlc.types.Field('DateTimeValueInput', graphql_name='endDate')
    access_level_id = sgqlc.types.Field(ID, graphql_name='accessLevelId')


class ConceptLinkFilterSettings(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('is_event', 'concept_link_type', 'document_id', 'creation_date', 'update_date')
    is_event = sgqlc.types.Field(Boolean, graphql_name='isEvent')
    concept_link_type = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='conceptLinkType')
    document_id = sgqlc.types.Field(ID, graphql_name='documentId')
    creation_date = sgqlc.types.Field('TimestampInterval', graphql_name='creationDate')
    update_date = sgqlc.types.Field('TimestampInterval', graphql_name='updateDate')


class ConceptLinkPropertyInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('property_type_id', 'fact_info', 'notes', 'value_input', 'computable_value', 'link_id', 'is_main', 'start_date', 'end_date', 'access_level_id')
    property_type_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='propertyTypeId')
    fact_info = sgqlc.types.Field('FactInput', graphql_name='factInfo')
    notes = sgqlc.types.Field(String, graphql_name='notes')
    value_input = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ComponentValueInput))), graphql_name='valueInput')
    computable_value = sgqlc.types.Field(String, graphql_name='computableValue')
    link_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='linkId')
    is_main = sgqlc.types.Field(Boolean, graphql_name='isMain')
    start_date = sgqlc.types.Field('DateTimeValueInput', graphql_name='startDate')
    end_date = sgqlc.types.Field('DateTimeValueInput', graphql_name='endDate')
    access_level_id = sgqlc.types.Field(ID, graphql_name='accessLevelId')


class ConceptLinkPropertyTypeCreationInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('link_type_id', 'name', 'value_type_id', 'computable_formula', 'pretrained_rel_ext_models', 'notify_on_update')
    link_type_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='linkTypeId')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    value_type_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='valueTypeId')
    computable_formula = sgqlc.types.Field(String, graphql_name='computableFormula')
    pretrained_rel_ext_models = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('RelExtModelInput')), graphql_name='pretrainedRelExtModels')
    notify_on_update = sgqlc.types.Field(Boolean, graphql_name='notifyOnUpdate')


class ConceptLinkPropertyTypeUpdateInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('id', 'name', 'value_type_id', 'computable_formula', 'pretrained_rel_ext_models', 'notify_on_update')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    value_type_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='valueTypeId')
    computable_formula = sgqlc.types.Field(String, graphql_name='computableFormula')
    pretrained_rel_ext_models = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('RelExtModelInput')), graphql_name='pretrainedRelExtModels')
    notify_on_update = sgqlc.types.Field(Boolean, graphql_name='notifyOnUpdate')


class ConceptLinkTypeCreationInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('name', 'is_directed', 'is_hierarchical', 'concept_from_type_id', 'concept_to_type_id', 'pretrained_rel_ext_models', 'notify_on_update')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    is_directed = sgqlc.types.Field(Boolean, graphql_name='isDirected')
    is_hierarchical = sgqlc.types.Field(Boolean, graphql_name='isHierarchical')
    concept_from_type_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='conceptFromTypeId')
    concept_to_type_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='conceptToTypeId')
    pretrained_rel_ext_models = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('RelExtModelInput')), graphql_name='pretrainedRelExtModels')
    notify_on_update = sgqlc.types.Field(Boolean, graphql_name='notifyOnUpdate')


class ConceptLinkTypeFilterSettings(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('name', 'concept_from_type_id', 'concept_to_type_id', 'concept_type_and_event_filter', 'is_directed', 'is_hierarchical', 'creator', 'last_updater', 'registration_date', 'update_date', 'has_rel_ext_models')
    name = sgqlc.types.Field(String, graphql_name='name')
    concept_from_type_id = sgqlc.types.Field(ID, graphql_name='conceptFromTypeId')
    concept_to_type_id = sgqlc.types.Field(ID, graphql_name='conceptToTypeId')
    concept_type_and_event_filter = sgqlc.types.Field('conceptTypeAndEventFilter', graphql_name='conceptTypeAndEventFilter')
    is_directed = sgqlc.types.Field(Boolean, graphql_name='isDirected')
    is_hierarchical = sgqlc.types.Field(Boolean, graphql_name='isHierarchical')
    creator = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='creator')
    last_updater = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='lastUpdater')
    registration_date = sgqlc.types.Field('TimestampInterval', graphql_name='registrationDate')
    update_date = sgqlc.types.Field('TimestampInterval', graphql_name='updateDate')
    has_rel_ext_models = sgqlc.types.Field(Boolean, graphql_name='hasRelExtModels')


class ConceptLinkTypePathInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('link_type_id', 'fixed')
    link_type_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='linkTypeId')
    fixed = sgqlc.types.Field(ConceptLinkDirection, graphql_name='fixed')


class ConceptLinkTypeUpdateInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('id', 'name', 'concept_from_type_id', 'concept_to_type_id', 'pretrained_rel_ext_models', 'is_directed', 'is_hierarchical', 'notify_on_update')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    concept_from_type_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='conceptFromTypeId')
    concept_to_type_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='conceptToTypeId')
    pretrained_rel_ext_models = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('RelExtModelInput')), graphql_name='pretrainedRelExtModels')
    is_directed = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isDirected')
    is_hierarchical = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isHierarchical')
    notify_on_update = sgqlc.types.Field(Boolean, graphql_name='notifyOnUpdate')


class ConceptLinkUpdateMutationInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('id', 'notes', 'start_date', 'end_date', 'access_level_id')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    notes = sgqlc.types.Field(String, graphql_name='notes')
    start_date = sgqlc.types.Field('DateTimeValueInput', graphql_name='startDate')
    end_date = sgqlc.types.Field('DateTimeValueInput', graphql_name='endDate')
    access_level_id = sgqlc.types.Field(ID, graphql_name='accessLevelId')


class ConceptMergeInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('main_concept_id', 'merged_concept_id')
    main_concept_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='mainConceptId')
    merged_concept_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='mergedConceptId')


class ConceptMutationInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('name', 'concept_type_id', 'notes', 'fact_info', 'markers', 'access_level_id', 'start_date', 'end_date')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    concept_type_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='conceptTypeId')
    notes = sgqlc.types.Field(String, graphql_name='notes')
    fact_info = sgqlc.types.Field('FactInput', graphql_name='factInfo')
    markers = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='markers')
    access_level_id = sgqlc.types.Field(ID, graphql_name='accessLevelId')
    start_date = sgqlc.types.Field('DateTimeValueInput', graphql_name='startDate')
    end_date = sgqlc.types.Field('DateTimeValueInput', graphql_name='endDate')


class ConceptPanelInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('filter_id',)
    filter_id = sgqlc.types.Field(ID, graphql_name='filterId')


class ConceptPropertyCreateInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('property_type_id', 'concept_id', 'value_input', 'computable_value', 'fact_info', 'notes', 'is_main', 'start_date', 'end_date', 'access_level_id')
    property_type_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='propertyTypeId')
    concept_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='conceptId')
    value_input = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ComponentValueInput))), graphql_name='valueInput')
    computable_value = sgqlc.types.Field(String, graphql_name='computableValue')
    fact_info = sgqlc.types.Field('FactInput', graphql_name='factInfo')
    notes = sgqlc.types.Field(String, graphql_name='notes')
    is_main = sgqlc.types.Field(Boolean, graphql_name='isMain')
    start_date = sgqlc.types.Field('DateTimeValueInput', graphql_name='startDate')
    end_date = sgqlc.types.Field('DateTimeValueInput', graphql_name='endDate')
    access_level_id = sgqlc.types.Field(ID, graphql_name='accessLevelId')


class ConceptPropertyFilterSettings(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('only_main', 'document_id')
    only_main = sgqlc.types.Field(Boolean, graphql_name='onlyMain')
    document_id = sgqlc.types.Field(ID, graphql_name='documentId')


class ConceptPropertyTypeCreationInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('concept_type_id', 'name', 'value_type_id', 'computable_formula', 'pretrained_rel_ext_models', 'notify_on_update')
    concept_type_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='conceptTypeId')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    value_type_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='valueTypeId')
    computable_formula = sgqlc.types.Field(String, graphql_name='computableFormula')
    pretrained_rel_ext_models = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('RelExtModelInput')), graphql_name='pretrainedRelExtModels')
    notify_on_update = sgqlc.types.Field(Boolean, graphql_name='notifyOnUpdate')


class ConceptPropertyTypeFilterSettings(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('name', 'concept_type_id', 'concept_link_type_id', 'concept_value_type_id', 'value_type', 'concept_type_from_link_type_id')
    name = sgqlc.types.Field(String, graphql_name='name')
    concept_type_id = sgqlc.types.Field(ID, graphql_name='conceptTypeId')
    concept_link_type_id = sgqlc.types.Field(ID, graphql_name='conceptLinkTypeId')
    concept_value_type_id = sgqlc.types.Field(ID, graphql_name='conceptValueTypeId')
    value_type = sgqlc.types.Field(ValueType, graphql_name='valueType')
    concept_type_from_link_type_id = sgqlc.types.Field(ID, graphql_name='conceptTypeFromLinkTypeId')


class ConceptPropertyTypeUpdateInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('id', 'name', 'value_type_id', 'computable_formula', 'pretrained_rel_ext_models', 'notify_on_update')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    value_type_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='valueTypeId')
    computable_formula = sgqlc.types.Field(String, graphql_name='computableFormula')
    pretrained_rel_ext_models = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('RelExtModelInput')), graphql_name='pretrainedRelExtModels')
    notify_on_update = sgqlc.types.Field(Boolean, graphql_name='notifyOnUpdate')


class ConceptPropertyUpdateInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('property_id', 'is_main', 'notes', 'computable_value', 'start_date', 'end_date', 'value_input', 'access_level_id')
    property_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='propertyId')
    is_main = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isMain')
    notes = sgqlc.types.Field(String, graphql_name='notes')
    computable_value = sgqlc.types.Field(String, graphql_name='computableValue')
    start_date = sgqlc.types.Field('DateTimeValueInput', graphql_name='startDate')
    end_date = sgqlc.types.Field('DateTimeValueInput', graphql_name='endDate')
    value_input = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ComponentValueInput))), graphql_name='valueInput')
    access_level_id = sgqlc.types.Field(ID, graphql_name='accessLevelId')


class ConceptPropertyValueTypeCreationInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('name', 'value_type', 'pretrained_nercmodels', 'value_restriction')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    value_type = sgqlc.types.Field(sgqlc.types.non_null(ValueType), graphql_name='valueType')
    pretrained_nercmodels = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='pretrainedNERCModels')
    value_restriction = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='valueRestriction')


class ConceptPropertyValueTypeFilterSettings(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('name', 'value_type', 'creator', 'last_updater', 'registration_date', 'update_date', 'regexp_exists', 'dictionary_exists', 'pretrained_nercmodels')
    name = sgqlc.types.Field(String, graphql_name='name')
    value_type = sgqlc.types.Field(ValueType, graphql_name='valueType')
    creator = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='creator')
    last_updater = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='lastUpdater')
    registration_date = sgqlc.types.Field('TimestampInterval', graphql_name='registrationDate')
    update_date = sgqlc.types.Field('TimestampInterval', graphql_name='updateDate')
    regexp_exists = sgqlc.types.Field(Boolean, graphql_name='regexpExists')
    dictionary_exists = sgqlc.types.Field(Boolean, graphql_name='dictionaryExists')
    pretrained_nercmodels = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='pretrainedNERCModels')


class ConceptPropertyValueTypeUpdateInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('id', 'name', 'value_type', 'pretrained_nercmodels', 'value_restriction')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    value_type = sgqlc.types.Field(sgqlc.types.non_null(ValueType), graphql_name='valueType')
    pretrained_nercmodels = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='pretrainedNERCModels')
    value_restriction = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='valueRestriction')


class ConceptRegistryViewInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('columns', 'metrics', 'sorting')
    columns = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ConceptViewColumnType)), graphql_name='columns')
    metrics = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ConceptViewMetricType)), graphql_name='metrics')
    sorting = sgqlc.types.Field('ConceptRegistryViewSortingInput', graphql_name='sorting')


class ConceptRegistryViewSortingInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('sorting_type', 'sort_direction')
    sorting_type = sgqlc.types.Field(sgqlc.types.non_null(ConceptSorting), graphql_name='sortingType')
    sort_direction = sgqlc.types.Field(sgqlc.types.non_null(SortDirection), graphql_name='sortDirection')


class ConceptTransformConfigFilter(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('system_registration_date', 'system_update_date', 'creator_id', 'last_updater_id', 'description', 'can_transform_one_entity', 'can_transform_multiple_entities', 'can_transform_concept_type_ids', 'can_be_used')
    system_registration_date = sgqlc.types.Field('TimestampInterval', graphql_name='systemRegistrationDate')
    system_update_date = sgqlc.types.Field('TimestampInterval', graphql_name='systemUpdateDate')
    creator_id = sgqlc.types.Field(ID, graphql_name='creatorId')
    last_updater_id = sgqlc.types.Field(ID, graphql_name='lastUpdaterId')
    description = sgqlc.types.Field(String, graphql_name='description')
    can_transform_one_entity = sgqlc.types.Field(Boolean, graphql_name='canTransformOneEntity')
    can_transform_multiple_entities = sgqlc.types.Field(Boolean, graphql_name='canTransformMultipleEntities')
    can_transform_concept_type_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='canTransformConceptTypeIds')
    can_be_used = sgqlc.types.Field(Boolean, graphql_name='canBeUsed')


class ConceptTransformConfigInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('title', 'description', 'concept_type_ids', 'can_transform_one_entity', 'can_transform_multiple_entities', 'priority')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    description = sgqlc.types.Field(String, graphql_name='description')
    concept_type_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='conceptTypeIds')
    can_transform_one_entity = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='canTransformOneEntity')
    can_transform_multiple_entities = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='canTransformMultipleEntities')
    priority = sgqlc.types.Field(Int, graphql_name='priority')


class ConceptTransformTaskFilter(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('config', 'creator_id', 'state', 'id', 'system_registration_date')
    config = sgqlc.types.Field(ID, graphql_name='config')
    creator_id = sgqlc.types.Field(ID, graphql_name='creatorId')
    state = sgqlc.types.Field(ConceptTransformTaskState, graphql_name='state')
    id = sgqlc.types.Field(ID, graphql_name='id')
    system_registration_date = sgqlc.types.Field('TimestampInterval', graphql_name='systemRegistrationDate')


class ConceptTransformTaskInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('config', 'concept_ids')
    config = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='config')
    concept_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='conceptIds')


class ConceptTypeCreationInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('name', 'x_coordinate', 'y_coordinate', 'pretrained_nercmodels', 'is_event', 'show_in_menu')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    x_coordinate = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='xCoordinate')
    y_coordinate = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='yCoordinate')
    pretrained_nercmodels = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='pretrainedNERCModels')
    is_event = sgqlc.types.Field(Boolean, graphql_name='isEvent')
    show_in_menu = sgqlc.types.Field(Boolean, graphql_name='showInMenu')


class ConceptTypeFilterSettings(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('name', 'is_event', 'creator', 'last_updater', 'registration_date', 'update_date', 'regexp_exists', 'dictionary_exists', 'pretrained_nercmodels')
    name = sgqlc.types.Field(String, graphql_name='name')
    is_event = sgqlc.types.Field(Boolean, graphql_name='isEvent')
    creator = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='creator')
    last_updater = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='lastUpdater')
    registration_date = sgqlc.types.Field('TimestampInterval', graphql_name='registrationDate')
    update_date = sgqlc.types.Field('TimestampInterval', graphql_name='updateDate')
    regexp_exists = sgqlc.types.Field(Boolean, graphql_name='regexpExists')
    dictionary_exists = sgqlc.types.Field(Boolean, graphql_name='dictionaryExists')
    pretrained_nercmodels = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='pretrainedNERCModels')


class ConceptTypeUpdateInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('id', 'x_coordinate', 'y_coordinate', 'name', 'pretrained_nercmodels', 'is_event', 'show_in_menu')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    x_coordinate = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='xCoordinate')
    y_coordinate = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='yCoordinate')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    pretrained_nercmodels = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='pretrainedNERCModels')
    is_event = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isEvent')
    show_in_menu = sgqlc.types.Field(Boolean, graphql_name='showInMenu')


class ConceptTypeViewCreationInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('concept_type_id', 'name', 'show_in_menu', 'columns')
    concept_type_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='conceptTypeId')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    show_in_menu = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='showInMenu')
    columns = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CompositeConceptTypeWidgetTypeColumnInput))), graphql_name='columns')


class ConceptTypeViewUpdateInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('id', 'name', 'show_in_menu', 'columns')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    show_in_menu = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='showInMenu')
    columns = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CompositeConceptTypeWidgetTypeColumnInput))), graphql_name='columns')


class ConceptUnmergeInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('main_concept_id', 'merged_concept_id')
    main_concept_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='mainConceptId')
    merged_concept_id = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='mergedConceptId')


class ConceptUpdateInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('concept_id', 'name', 'concept_type_id', 'notes', 'document_input', 'markers', 'access_level_id', 'start_date', 'end_date')
    concept_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='conceptId')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    concept_type_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='conceptTypeId')
    notes = sgqlc.types.Field(String, graphql_name='notes')
    document_input = sgqlc.types.Field('FactInput', graphql_name='documentInput')
    markers = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='markers')
    access_level_id = sgqlc.types.Field(ID, graphql_name='accessLevelId')
    start_date = sgqlc.types.Field('DateTimeValueInput', graphql_name='startDate')
    end_date = sgqlc.types.Field('DateTimeValueInput', graphql_name='endDate')


class ConceptViewPanelInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('id', 'concept_type_id')
    id = sgqlc.types.Field(ID, graphql_name='id')
    concept_type_id = sgqlc.types.Field(ID, graphql_name='conceptTypeId')


class Coordinate(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('x', 'y')
    x = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='x')
    y = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='y')


class CoordinatesInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('latitude', 'longitude')
    latitude = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='latitude')
    longitude = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='longitude')


class CountryFilterSettings(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('search_string', 'target')
    search_string = sgqlc.types.Field(String, graphql_name='searchString')
    target = sgqlc.types.Field(CountryTarget, graphql_name='target')


class CrawlerFilterSettings(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('input_value', 'projects', 'crawlers_types', 'last_collection_date', 'created_by', 'changed_by', 'created_at', 'changed_at', 'have_active_versions')
    input_value = sgqlc.types.Field(String, graphql_name='inputValue')
    projects = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='projects')
    crawlers_types = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(CrawlersType)), graphql_name='crawlersTypes')
    last_collection_date = sgqlc.types.Field('TimestampInterval', graphql_name='lastCollectionDate')
    created_by = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='createdBy')
    changed_by = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='changedBy')
    created_at = sgqlc.types.Field('TimestampInterval', graphql_name='createdAt')
    changed_at = sgqlc.types.Field('TimestampInterval', graphql_name='changedAt')
    have_active_versions = sgqlc.types.Field(Boolean, graphql_name='haveActiveVersions')


class CrawlerInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class CrawlerUpdateInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('project_id', 'title', 'description', 'settings', 'args', 'state', 'state_version')
    project_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='projectId')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    description = sgqlc.types.Field(String, graphql_name='description')
    settings = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('KeyValueInputType'))), graphql_name='settings')
    args = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('KeyValueInputType'))), graphql_name='args')
    state = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('KeyValueInputType'))), graphql_name='state')
    state_version = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='stateVersion')


class CreateUserGroupParams(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('name', 'description')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    description = sgqlc.types.Field(String, graphql_name='description')


class CreateUserParams(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('login', 'first_name', 'last_name', 'fathers_name', 'email', 'access_level_id', 'is_admin', 'redmine_api_key', 'enabled', 'receive_notifications')
    login = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='login')
    first_name = sgqlc.types.Field(String, graphql_name='firstName')
    last_name = sgqlc.types.Field(String, graphql_name='lastName')
    fathers_name = sgqlc.types.Field(String, graphql_name='fathersName')
    email = sgqlc.types.Field(String, graphql_name='email')
    access_level_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='accessLevelID')
    is_admin = sgqlc.types.Field(Boolean, graphql_name='isAdmin')
    redmine_api_key = sgqlc.types.Field(String, graphql_name='redmineApiKey')
    enabled = sgqlc.types.Field(Boolean, graphql_name='enabled')
    receive_notifications = sgqlc.types.Field(Boolean, graphql_name='receiveNotifications')


class CredentialFilterSettings(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('input_value', 'projects', 'status', 'data_type', 'created_by', 'changed_by', 'created_at', 'changed_at')
    input_value = sgqlc.types.Field(String, graphql_name='inputValue')
    projects = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='projects')
    status = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(CredentialStatus)), graphql_name='status')
    data_type = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(CredentialType)), graphql_name='dataType')
    created_by = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='createdBy')
    changed_by = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='changedBy')
    created_at = sgqlc.types.Field('TimestampInterval', graphql_name='createdAt')
    changed_at = sgqlc.types.Field('TimestampInterval', graphql_name='changedAt')


class CredentialInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('projects', 'status', 'domain', 'description', 'data_type', 'login', 'password', 'token', 'state', 'cookies')
    projects = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='projects')
    status = sgqlc.types.Field(CredentialStatus, graphql_name='status')
    domain = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='domain')
    description = sgqlc.types.Field(String, graphql_name='description')
    data_type = sgqlc.types.Field(sgqlc.types.non_null(CredentialType), graphql_name='dataType')
    login = sgqlc.types.Field(String, graphql_name='login')
    password = sgqlc.types.Field(String, graphql_name='password')
    token = sgqlc.types.Field(String, graphql_name='token')
    state = sgqlc.types.Field(JSON, graphql_name='state')
    cookies = sgqlc.types.Field(JSON, graphql_name='cookies')


class DBConfigInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('url', 'login', 'password', 'db_query_type', 'sql_query', 'target_table', 'file_columns')
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')
    login = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='login')
    password = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='password')
    db_query_type = sgqlc.types.Field(sgqlc.types.non_null(QueryType), graphql_name='dbQueryType')
    sql_query = sgqlc.types.Field(String, graphql_name='sqlQuery')
    target_table = sgqlc.types.Field(String, graphql_name='targetTable')
    file_columns = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('FileQueryInput'))), graphql_name='fileColumns')


class DashboardInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('name', 'description', 'is_main', 'refresh_time', 'shared')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='description')
    is_main = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isMain')
    refresh_time = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='refreshTime')
    shared = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='shared')


class DashboardLayoutItemInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('i', 'x', 'y', 'w', 'h', 'min_w', 'max_w', 'min_h', 'max_h', 'static', 'is_draggable', 'is_resizable', 'moved')
    i = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='i')
    x = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='x')
    y = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='y')
    w = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='w')
    h = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='h')
    min_w = sgqlc.types.Field(Int, graphql_name='minW')
    max_w = sgqlc.types.Field(Int, graphql_name='maxW')
    min_h = sgqlc.types.Field(Int, graphql_name='minH')
    max_h = sgqlc.types.Field(Int, graphql_name='maxH')
    static = sgqlc.types.Field(Boolean, graphql_name='static')
    is_draggable = sgqlc.types.Field(Boolean, graphql_name='isDraggable')
    is_resizable = sgqlc.types.Field(Boolean, graphql_name='isResizable')
    moved = sgqlc.types.Field(Boolean, graphql_name='moved')


class DashboardPanelDataInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('task', 'concept', 'document', 'concept_view', 'chart')
    task = sgqlc.types.Field('TaskPanelInput', graphql_name='task')
    concept = sgqlc.types.Field(ConceptPanelInput, graphql_name='concept')
    document = sgqlc.types.Field('DocumentPanelInput', graphql_name='document')
    concept_view = sgqlc.types.Field(ConceptViewPanelInput, graphql_name='conceptView')
    chart = sgqlc.types.Field(ChartPanelInput, graphql_name='chart')


class DashboardPanelInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('label', 'data', 'data_type')
    label = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='label')
    data = sgqlc.types.Field(sgqlc.types.non_null(DashboardPanelDataInput), graphql_name='data')
    data_type = sgqlc.types.Field(DashboardPanelType, graphql_name='dataType')


class DateInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('day', 'month', 'year')
    day = sgqlc.types.Field(Int, graphql_name='day')
    month = sgqlc.types.Field(Int, graphql_name='month')
    year = sgqlc.types.Field(Int, graphql_name='year')


class DateTimeIntervalInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('start', 'end')
    start = sgqlc.types.Field('DateTimeValueInput', graphql_name='start')
    end = sgqlc.types.Field('DateTimeValueInput', graphql_name='end')


class DateTimeIntervalPairInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('start', 'end')
    start = sgqlc.types.Field(sgqlc.types.non_null(DateTimeIntervalInput), graphql_name='start')
    end = sgqlc.types.Field(sgqlc.types.non_null(DateTimeIntervalInput), graphql_name='end')


class DateTimeValueInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('date', 'time')
    date = sgqlc.types.Field(sgqlc.types.non_null(DateInput), graphql_name='date')
    time = sgqlc.types.Field('TimeInput', graphql_name='time')


class DeleteUserGroupMemberParams(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('user_id', 'group_id')
    user_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='userId')
    group_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='groupId')


class Document2IssueInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('id_issue', 'document_ids', 'comment')
    id_issue = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='idIssue')
    document_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='documentIds')
    comment = sgqlc.types.Field(String, graphql_name='comment')


class DocumentAddInputInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('document_id', 'x_coordinate', 'y_coordinate', 'group_id')
    document_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='documentId')
    x_coordinate = sgqlc.types.Field(Float, graphql_name='xCoordinate')
    y_coordinate = sgqlc.types.Field(Float, graphql_name='yCoordinate')
    group_id = sgqlc.types.Field(ID, graphql_name='groupId')


class DocumentAllKBFactsRemoveInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('document_id', 'kb_entity_id')
    document_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='documentId')
    kb_entity_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='kbEntityId')


class DocumentAvatarUpdateInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('id', 'children_document_id')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    children_document_id = sgqlc.types.Field(ID, graphql_name='childrenDocumentId')


class DocumentCardViewInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('columns', 'metrics')
    columns = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(DocumentViewColumnType)), graphql_name='columns')
    metrics = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(DocumentViewMetricType)), graphql_name='metrics')


class DocumentDeleteCandidateFactInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('document_id', 'fact_id')
    document_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='documentId')
    fact_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='factId')


class DocumentDoubleCreationInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('uuid', 'double_uuid', 'parent_uuid', 'concept_id')
    uuid = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='uuid')
    double_uuid = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='doubleUuid')
    parent_uuid = sgqlc.types.Field(ID, graphql_name='parentUuid')
    concept_id = sgqlc.types.Field(ID, graphql_name='conceptId')


class DocumentFeedCreationInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('name', 'query', 'filter_settings')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    query = sgqlc.types.Field(String, graphql_name='query')
    filter_settings = sgqlc.types.Field('DocumentFilterSettings', graphql_name='filterSettings')


class DocumentFeedFilterSettings(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('id', 'search_string', 'creator', 'last_updater', 'registration_date', 'update_date')
    id = sgqlc.types.Field(ID, graphql_name='id')
    search_string = sgqlc.types.Field(String, graphql_name='searchString')
    creator = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='creator')
    last_updater = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='lastUpdater')
    registration_date = sgqlc.types.Field('TimestampInterval', graphql_name='registrationDate')
    update_date = sgqlc.types.Field('TimestampInterval', graphql_name='updateDate')


class DocumentFeedUpdateDocumentsInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('document_ids',)
    document_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='documentIds')


class DocumentFeedUpdateInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('name', 'query', 'filter_settings')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    query = sgqlc.types.Field(String, graphql_name='query')
    filter_settings = sgqlc.types.Field('DocumentFilterSettings', graphql_name='filterSettings')


class DocumentFilterSettings(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('search_string', 'substring', 'named_entities', 'concepts', 'platforms', 'accounts', 'nerc_num', 'concepts_num', 'child_docs_num', 'publication_date', 'registration_date', 'last_update', 'creator', 'publication_author', 'last_updater', 'access_level_id', 'links', 'markers', 'document_type', 'source_type', 'trust_level', 'has_linked_issues', 'nested_ids', 'fact_types', 'story', 'show_read', 'job_ids', 'periodic_job_ids', 'task_ids', 'periodic_task_ids')
    search_string = sgqlc.types.Field(String, graphql_name='searchString')
    substring = sgqlc.types.Field(String, graphql_name='substring')
    named_entities = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='namedEntities')
    concepts = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='concepts')
    platforms = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='platforms')
    accounts = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='accounts')
    nerc_num = sgqlc.types.Field('IntervalInt', graphql_name='nercNum')
    concepts_num = sgqlc.types.Field('IntervalInt', graphql_name='conceptsNum')
    child_docs_num = sgqlc.types.Field('IntervalInt', graphql_name='childDocsNum')
    publication_date = sgqlc.types.Field('TimestampInterval', graphql_name='publicationDate')
    registration_date = sgqlc.types.Field('TimestampInterval', graphql_name='registrationDate')
    last_update = sgqlc.types.Field('TimestampInterval', graphql_name='lastUpdate')
    creator = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='creator')
    publication_author = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='publicationAuthor')
    last_updater = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='lastUpdater')
    access_level_id = sgqlc.types.Field(ID, graphql_name='accessLevelId')
    links = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='links')
    markers = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='markers')
    document_type = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(DocumentType)), graphql_name='documentType')
    source_type = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(DocumentSourceType)), graphql_name='sourceType')
    trust_level = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(TrustLevel)), graphql_name='trustLevel')
    has_linked_issues = sgqlc.types.Field(Boolean, graphql_name='hasLinkedIssues')
    nested_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='nestedIds')
    fact_types = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='factTypes')
    story = sgqlc.types.Field(String, graphql_name='story')
    show_read = sgqlc.types.Field(Boolean, graphql_name='showRead')
    job_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='jobIds')
    periodic_job_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='periodicJobIds')
    task_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='taskIds')
    periodic_task_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='periodicTaskIds')


class DocumentLinkFilterSetting(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('document_type',)
    document_type = sgqlc.types.Field(DocumentType, graphql_name='documentType')


class DocumentNodeUpdateInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('id', 'node_id', 'language', 'translation')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    node_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='nodeId')
    language = sgqlc.types.Field('LanguageUpdateInput', graphql_name='language')
    translation = sgqlc.types.Field('TranslationInput', graphql_name='translation')


class DocumentPanelInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('filter_id', 'direction', 'sort_field')
    filter_id = sgqlc.types.Field(ID, graphql_name='filterId')
    direction = sgqlc.types.Field(SortDirection, graphql_name='direction')
    sort_field = sgqlc.types.Field(DocumentSorting, graphql_name='sortField')


class DocumentRegistryViewInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('columns', 'metrics', 'sorting')
    columns = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(DocumentViewColumnType)), graphql_name='columns')
    metrics = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(DocumentViewMetricType)), graphql_name='metrics')
    sorting = sgqlc.types.Field('DocumentRegistryViewSortingInput', graphql_name='sorting')


class DocumentRegistryViewSortingInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('sorting_type', 'sort_direction')
    sorting_type = sgqlc.types.Field(sgqlc.types.non_null(DocumentSorting), graphql_name='sortingType')
    sort_direction = sgqlc.types.Field(sgqlc.types.non_null(SortDirection), graphql_name='sortDirection')


class DocumentUpdateInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('id', 'notes', 'title', 'preview_text', 'publication_date', 'publication_author', 'markers', 'trust_level', 'platform', 'account', 'language')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    notes = sgqlc.types.Field(String, graphql_name='notes')
    title = sgqlc.types.Field(String, graphql_name='title')
    preview_text = sgqlc.types.Field(String, graphql_name='previewText')
    publication_date = sgqlc.types.Field(Long, graphql_name='publicationDate')
    publication_author = sgqlc.types.Field(String, graphql_name='publicationAuthor')
    markers = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='markers')
    trust_level = sgqlc.types.Field(TrustLevel, graphql_name='trustLevel')
    platform = sgqlc.types.Field(ID, graphql_name='platform')
    account = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='account')
    language = sgqlc.types.Field(String, graphql_name='language')


class DoubleValueInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('value',)
    value = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='value')


class EventFilterSettings(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('date_time', 'level', 'is_read')
    date_time = sgqlc.types.Field('TimestampInterval', graphql_name='dateTime')
    level = sgqlc.types.Field(EventLevel, graphql_name='level')
    is_read = sgqlc.types.Field(Boolean, graphql_name='isRead')


class ExportEntityInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('type', 'id')
    type = sgqlc.types.Field(sgqlc.types.non_null(ExportEntityType), graphql_name='type')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class ExportTaskFilter(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('exporter', 'creator_id', 'state', 'id', 'system_registration_date')
    exporter = sgqlc.types.Field(ID, graphql_name='exporter')
    creator_id = sgqlc.types.Field(ID, graphql_name='creatorId')
    state = sgqlc.types.Field(ExportTaskState, graphql_name='state')
    id = sgqlc.types.Field(ID, graphql_name='id')
    system_registration_date = sgqlc.types.Field('TimestampInterval', graphql_name='systemRegistrationDate')


class ExportTaskInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('entities', 'params')
    entities = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ExportEntityInput))), graphql_name='entities')
    params = sgqlc.types.Field(sgqlc.types.non_null(JSON), graphql_name='params')


class ExporterFilter(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('can_export_document', 'can_export_concept', 'can_export_one_entity', 'can_export_multiple_entities', 'can_export_concept_type_ids')
    can_export_document = sgqlc.types.Field(Boolean, graphql_name='canExportDocument')
    can_export_concept = sgqlc.types.Field(Boolean, graphql_name='canExportConcept')
    can_export_one_entity = sgqlc.types.Field(Boolean, graphql_name='canExportOneEntity')
    can_export_multiple_entities = sgqlc.types.Field(Boolean, graphql_name='canExportMultipleEntities')
    can_export_concept_type_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='canExportConceptTypeIds')


class ExporterInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('menu_title', 'description', 'default_params', 'can_export_one_entity', 'can_export_multiple_entities', 'concept_type_ids')
    menu_title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='menuTitle')
    description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='description')
    default_params = sgqlc.types.Field(JSON, graphql_name='defaultParams')
    can_export_one_entity = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='canExportOneEntity')
    can_export_multiple_entities = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='canExportMultipleEntities')
    concept_type_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='conceptTypeIds')


class ExternalSearchJobConfigInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('crawler', 'version', 'args', 'settings', 'noisy_jobs_count', 'update_on_reload', 'concept_type_id')
    crawler = sgqlc.types.Field(sgqlc.types.non_null(CrawlerInput), graphql_name='crawler')
    version = sgqlc.types.Field(sgqlc.types.non_null('VersionInput'), graphql_name='version')
    args = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('KeyValueInput'))), graphql_name='args')
    settings = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('KeyValueInput'))), graphql_name='settings')
    noisy_jobs_count = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='noisyJobsCount')
    update_on_reload = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateOnReload')
    concept_type_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='conceptTypeId')


class ExtraSettings(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('hide_child', 'search_on_map', 'ranking_script', 'selected_content')
    hide_child = sgqlc.types.Field(Boolean, graphql_name='hideChild')
    search_on_map = sgqlc.types.Field(Boolean, graphql_name='searchOnMap')
    ranking_script = sgqlc.types.Field(String, graphql_name='rankingScript')
    selected_content = sgqlc.types.Field('ResearchMapContentSelectInput', graphql_name='selectedContent')


class FactInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('document_id', 'annotations', 'fact_id')
    document_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='documentId')
    annotations = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('TextBoundingInput')), graphql_name='annotations')
    fact_id = sgqlc.types.Field(ID, graphql_name='factId')


class FileQueryInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('name_column', 'data_column', 'is_main_file')
    name_column = sgqlc.types.Field(String, graphql_name='nameColumn')
    data_column = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='dataColumn')
    is_main_file = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isMainFile')


class FileRepositoryConfigInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('url', 'domain', 'login', 'password', 'delete_info_from_resource', 'recursive_traversal')
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')
    domain = sgqlc.types.Field(String, graphql_name='domain')
    login = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='login')
    password = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='password')
    delete_info_from_resource = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteInfoFromResource')
    recursive_traversal = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='recursiveTraversal')


class FileSettings(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('file_id', 'is_first_row_title', 'is_site_name_not_exist')
    file_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='fileId')
    is_first_row_title = sgqlc.types.Field(Boolean, graphql_name='isFirstRowTitle')
    is_site_name_not_exist = sgqlc.types.Field(Boolean, graphql_name='isSiteNameNotExist')


class FilterSettingsInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('fs', 'concept_id')
    fs = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='fs')
    concept_id = sgqlc.types.Field(ID, graphql_name='conceptId')


class GeoPointFormInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('latitude', 'longitude')
    latitude = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='latitude')
    longitude = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='longitude')


class GeoPointInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('point', 'name')
    point = sgqlc.types.Field(CoordinatesInput, graphql_name='point')
    name = sgqlc.types.Field(String, graphql_name='name')


class GeoPointWithNameFormInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('point', 'name', 'radius')
    point = sgqlc.types.Field(GeoPointFormInput, graphql_name='point')
    name = sgqlc.types.Field(String, graphql_name='name')
    radius = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='radius')


class GroupCreationInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('research_map_id', 'name', 'x_coordinate', 'y_coordinate', 'collapsed', 'layout')
    research_map_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='researchMapId')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    x_coordinate = sgqlc.types.Field(Float, graphql_name='xCoordinate')
    y_coordinate = sgqlc.types.Field(Float, graphql_name='yCoordinate')
    collapsed = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='collapsed')
    layout = sgqlc.types.Field(String, graphql_name='layout')


class GroupUpdateInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('name', 'x_coordinate', 'y_coordinate', 'collapsed', 'layout')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    x_coordinate = sgqlc.types.Field(Float, graphql_name='xCoordinate')
    y_coordinate = sgqlc.types.Field(Float, graphql_name='yCoordinate')
    collapsed = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='collapsed')
    layout = sgqlc.types.Field(String, graphql_name='layout')


class IndustryFilterSettings(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('search',)
    search = sgqlc.types.Field(String, graphql_name='search')


class InformationSourceFilterSettings(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('input_value', 'status')
    input_value = sgqlc.types.Field(String, graphql_name='inputValue')
    status = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(CollectionStatus)), graphql_name='status')


class InformationSourceLoaderFilterSettings(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('input_value', 'type_of_crawl', 'status', 'created_by', 'changed_by', 'created_at', 'changed_at')
    input_value = sgqlc.types.Field(String, graphql_name='inputValue')
    type_of_crawl = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(TypeOfCrawl)), graphql_name='typeOfCrawl')
    status = sgqlc.types.Field(CollectionStatus, graphql_name='status')
    created_by = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='createdBy')
    changed_by = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='changedBy')
    created_at = sgqlc.types.Field('TimestampInterval', graphql_name='createdAt')
    changed_at = sgqlc.types.Field('TimestampInterval', graphql_name='changedAt')


class InformationSourceLoaderInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('file_settings', 'urls', 'is_retrospective', 'retrospective_interval', 'actual_status')
    file_settings = sgqlc.types.Field(FileSettings, graphql_name='fileSettings')
    urls = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('KeyOptionValueInput')), graphql_name='urls')
    is_retrospective = sgqlc.types.Field(Boolean, graphql_name='isRetrospective')
    retrospective_interval = sgqlc.types.Field('TimestampInterval', graphql_name='retrospectiveInterval')
    actual_status = sgqlc.types.Field(InformationSourceLoaderActualStatus, graphql_name='actualStatus')


class IntValueInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('value',)
    value = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='value')


class InterestObjectMainPropertiesOrderUpdateInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('concept_type_id', 'ordered_main_property_type_ids')
    concept_type_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='conceptTypeId')
    ordered_main_property_type_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='orderedMainPropertyTypeIds')


class IntervalDouble(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('start', 'end')
    start = sgqlc.types.Field(Float, graphql_name='start')
    end = sgqlc.types.Field(Float, graphql_name='end')


class IntervalInt(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('start', 'end')
    start = sgqlc.types.Field(Int, graphql_name='start')
    end = sgqlc.types.Field(Int, graphql_name='end')


class Issue2TaskInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('id_issue', 'task_ids', 'comment')
    id_issue = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='idIssue')
    task_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='taskIds')
    comment = sgqlc.types.Field(String, graphql_name='comment')


class IssueCreationInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('topic', 'description', 'status', 'priority', 'executor_id', 'execution_time_limit', 'documents', 'concepts', 'issues', 'markers')
    topic = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='topic')
    description = sgqlc.types.Field(String, graphql_name='description')
    status = sgqlc.types.Field(sgqlc.types.non_null(IssueStatus), graphql_name='status')
    priority = sgqlc.types.Field(sgqlc.types.non_null(IssuePriority), graphql_name='priority')
    executor_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='executorId')
    execution_time_limit = sgqlc.types.Field(UnixTime, graphql_name='executionTimeLimit')
    documents = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='documents')
    concepts = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='concepts')
    issues = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='issues')
    markers = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='markers')


class IssueEditFieldsInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('id', 'topic', 'description', 'status', 'priority', 'executor_id', 'execution_time_limit', 'markers', 'comment')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    topic = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='topic')
    description = sgqlc.types.Field(String, graphql_name='description')
    status = sgqlc.types.Field(sgqlc.types.non_null(IssueStatus), graphql_name='status')
    priority = sgqlc.types.Field(sgqlc.types.non_null(IssuePriority), graphql_name='priority')
    executor_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='executorId')
    execution_time_limit = sgqlc.types.Field(UnixTime, graphql_name='executionTimeLimit')
    markers = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='markers')
    comment = sgqlc.types.Field(String, graphql_name='comment')


class IssueFilterSettings(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('executor', 'creator', 'last_updater', 'status', 'priority', 'registration_date', 'update_date', 'issue_for_document', 'issue_for_concept', 'only_my', 'issue', 'concept', 'document', 'name', 'description', 'execution_time_limit', 'markers')
    executor = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='executor')
    creator = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='creator')
    last_updater = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='lastUpdater')
    status = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IssueStatus)), graphql_name='status')
    priority = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IssuePriority)), graphql_name='priority')
    registration_date = sgqlc.types.Field('TimestampInterval', graphql_name='registrationDate')
    update_date = sgqlc.types.Field('TimestampInterval', graphql_name='updateDate')
    issue_for_document = sgqlc.types.Field(Boolean, graphql_name='issueForDocument')
    issue_for_concept = sgqlc.types.Field(Boolean, graphql_name='issueForConcept')
    only_my = sgqlc.types.Field(Boolean, graphql_name='onlyMy')
    issue = sgqlc.types.Field(ID, graphql_name='issue')
    concept = sgqlc.types.Field(ID, graphql_name='concept')
    document = sgqlc.types.Field(ID, graphql_name='document')
    name = sgqlc.types.Field(String, graphql_name='name')
    description = sgqlc.types.Field(String, graphql_name='description')
    execution_time_limit = sgqlc.types.Field('TimestampInterval', graphql_name='executionTimeLimit')
    markers = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='markers')


class ItemsFilter(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('input_text', 'interval', 'topic')
    input_text = sgqlc.types.Field(String, graphql_name='inputText')
    interval = sgqlc.types.Field('TimestampInterval', graphql_name='interval')
    topic = sgqlc.types.Field(String, graphql_name='topic')


class JobInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('crawler_id', 'version_id', 'priority', 'is_noise', 'settings', 'args')
    crawler_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='crawlerId')
    version_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='versionId')
    priority = sgqlc.types.Field(sgqlc.types.non_null(JobPriorityType), graphql_name='priority')
    is_noise = sgqlc.types.Field(Boolean, graphql_name='isNoise')
    settings = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('KeyValueInputType'))), graphql_name='settings')
    args = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('KeyValueInputType'))), graphql_name='args')


class JobSorting(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('job_pending_sorting', 'job_running_sorting', 'job_finished_sorting')
    job_pending_sorting = sgqlc.types.Field('JobsPendingSort', graphql_name='jobPendingSorting')
    job_running_sorting = sgqlc.types.Field('JobsRunningSort', graphql_name='jobRunningSorting')
    job_finished_sorting = sgqlc.types.Field('JobsFinishedSort', graphql_name='jobFinishedSorting')


class JobsFilter(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('input_value', 'projects', 'crawlers', 'created_by', 'changed_by', 'created_at', 'changed_at', 'periodic_jobs', 'collection_statuses', 'job_ids', 'start_time', 'end_time')
    input_value = sgqlc.types.Field(String, graphql_name='inputValue')
    projects = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='projects')
    crawlers = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='crawlers')
    created_by = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='createdBy')
    changed_by = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='changedBy')
    created_at = sgqlc.types.Field('TimestampInterval', graphql_name='createdAt')
    changed_at = sgqlc.types.Field('TimestampInterval', graphql_name='changedAt')
    periodic_jobs = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='periodicJobs')
    collection_statuses = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(CollectionStatus)), graphql_name='collectionStatuses')
    job_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Long)), graphql_name='jobIds')
    start_time = sgqlc.types.Field('TimestampInterval', graphql_name='startTime')
    end_time = sgqlc.types.Field('TimestampInterval', graphql_name='endTime')


class JobsFinishedSort(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('sort', 'direction')
    sort = sgqlc.types.Field(JobFinishedSort, graphql_name='sort')
    direction = sgqlc.types.Field(SortDirection, graphql_name='direction')


class JobsPendingSort(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('sort', 'direction')
    sort = sgqlc.types.Field(JobPendingSort, graphql_name='sort')
    direction = sgqlc.types.Field(SortDirection, graphql_name='direction')


class JobsRunningSort(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('sort', 'direction')
    sort = sgqlc.types.Field(JobRunningSort, graphql_name='sort')
    direction = sgqlc.types.Field(SortDirection, graphql_name='direction')


class KafkaTopicFilter(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('name', 'system_registration_date', 'system_update_date', 'creator_id', 'last_updater_id', 'description', 'pipeline_config', 'pipeline_config_description')
    name = sgqlc.types.Field(String, graphql_name='name')
    system_registration_date = sgqlc.types.Field('TimestampInterval', graphql_name='systemRegistrationDate')
    system_update_date = sgqlc.types.Field('TimestampInterval', graphql_name='systemUpdateDate')
    creator_id = sgqlc.types.Field(ID, graphql_name='creatorId')
    last_updater_id = sgqlc.types.Field(ID, graphql_name='lastUpdaterId')
    description = sgqlc.types.Field(String, graphql_name='description')
    pipeline_config = sgqlc.types.Field(ID, graphql_name='pipelineConfig')
    pipeline_config_description = sgqlc.types.Field(String, graphql_name='pipelineConfigDescription')


class KafkaTopicUpdate(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('description', 'clear_description', 'pipeline', 'clear_pipeline', 'priority', 'request_timeout_ms', 'clear_request_timeout_ms', 'move_to_on_timeout', 'clear_move_to_on_timeout')
    description = sgqlc.types.Field(String, graphql_name='description')
    clear_description = sgqlc.types.Field(Boolean, graphql_name='clearDescription')
    pipeline = sgqlc.types.Field('PipelineSetupInput', graphql_name='pipeline')
    clear_pipeline = sgqlc.types.Field(Boolean, graphql_name='clearPipeline')
    priority = sgqlc.types.Field(Int, graphql_name='priority')
    request_timeout_ms = sgqlc.types.Field(Int, graphql_name='requestTimeoutMs')
    clear_request_timeout_ms = sgqlc.types.Field(Boolean, graphql_name='clearRequestTimeoutMs')
    move_to_on_timeout = sgqlc.types.Field(String, graphql_name='moveToOnTimeout')
    clear_move_to_on_timeout = sgqlc.types.Field(Boolean, graphql_name='clearMoveToOnTimeout')


class KeyOptionValueInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('key', 'value')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')
    value = sgqlc.types.Field(String, graphql_name='value')


class KeyValueInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('key', 'value')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')
    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='value')


class KeyValueInputType(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('key', 'value')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')
    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='value')


class LanguageFilterSettings(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('search_string',)
    search_string = sgqlc.types.Field(String, graphql_name='searchString')


class LanguageInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class LanguageUpdateInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('id',)
    id = sgqlc.types.Field(ID, graphql_name='id')


class LinkFilterSettings(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('link_type_id', 'link_direction', 'other_concept_id')
    link_type_id = sgqlc.types.Field(ID, graphql_name='linkTypeId')
    link_direction = sgqlc.types.Field(LinkDirection, graphql_name='linkDirection')
    other_concept_id = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='otherConceptId')


class LinkValueInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('link',)
    link = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='link')


class LogFilterSettings(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('input_text', 'levels', 'interval')
    input_text = sgqlc.types.Field(String, graphql_name='inputText')
    levels = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(LogLevel)), graphql_name='levels')
    interval = sgqlc.types.Field('TimestampInterval', graphql_name='interval')


class MapEdgeFilterSettings(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('edge_type',)
    edge_type = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(MapEdgeType)), graphql_name='edgeType')


class MapNodeFilterSettings(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('node_type',)
    node_type = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(MapNodeType)), graphql_name='nodeType')


class MassUpdateIssueInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('ids', 'status', 'priority', 'executor', 'execution_time_limit', 'comment')
    ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids')
    status = sgqlc.types.Field(IssueStatus, graphql_name='status')
    priority = sgqlc.types.Field(IssuePriority, graphql_name='priority')
    executor = sgqlc.types.Field(ID, graphql_name='executor')
    execution_time_limit = sgqlc.types.Field(UnixTime, graphql_name='executionTimeLimit')
    comment = sgqlc.types.Field(String, graphql_name='comment')


class MessageFilter(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('id', 'input_text', 'parent_id', 'parent_or_self_id')
    id = sgqlc.types.Field(String, graphql_name='id')
    input_text = sgqlc.types.Field(String, graphql_name='inputText')
    parent_id = sgqlc.types.Field(String, graphql_name='parentId')
    parent_or_self_id = sgqlc.types.Field(String, graphql_name='parentOrSelfId')


class MetricFilterSettings(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('input_text', 'interval')
    input_text = sgqlc.types.Field(String, graphql_name='inputText')
    interval = sgqlc.types.Field('TimestampInterval', graphql_name='interval')


class MinioFile(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('bucket_name', 'object_name')
    bucket_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='bucketName')
    object_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='objectName')


class NERCRegexpInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('regexp', 'context_regexp', 'auto_create')
    regexp = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='regexp')
    context_regexp = sgqlc.types.Field(String, graphql_name='contextRegexp')
    auto_create = sgqlc.types.Field(Boolean, graphql_name='autoCreate')


class NamedValueType(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('name', 'value_type_id', 'view', 'is_required')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    value_type_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='valueTypeId')
    view = sgqlc.types.Field(ComponentView, graphql_name='view')
    is_required = sgqlc.types.Field(Boolean, graphql_name='isRequired')


class NodeMoveInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('id', 'x_coordinate', 'y_coordinate')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    x_coordinate = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='xCoordinate')
    y_coordinate = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='yCoordinate')


class NormalizationInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('type_id', 'value')
    type_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='typeId')
    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='value')


class OutputLimiterInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('maximum_points', 'minimum_number')
    maximum_points = sgqlc.types.Field(Long, graphql_name='maximumPoints')
    minimum_number = sgqlc.types.Field(Long, graphql_name='minimumNumber')


class PaginationAPTGroupsFilterSettings(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('name', 'date_interval', 'aggregation_type', 'severity_classes')
    name = sgqlc.types.Field(String, graphql_name='name')
    date_interval = sgqlc.types.Field(DateTimeIntervalInput, graphql_name='dateInterval')
    aggregation_type = sgqlc.types.Field(AggregationType, graphql_name='aggregationType')
    severity_classes = sgqlc.types.Field(sgqlc.types.list_of(SeverityCategories), graphql_name='severityClasses')


class PaginationCWEFilterSettings(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('name',)
    name = sgqlc.types.Field(String, graphql_name='name')


class PaginationExploitNamesFilterSettings(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('name',)
    name = sgqlc.types.Field(String, graphql_name='name')


class PaginationExploitsFilterSettings(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('name', 'date_interval', 'aggregation_type', 'cvss3_interval', 'integral_interval', 'soft_list', 'severity_classes')
    name = sgqlc.types.Field(String, graphql_name='name')
    date_interval = sgqlc.types.Field(DateTimeIntervalInput, graphql_name='dateInterval')
    aggregation_type = sgqlc.types.Field(AggregationType, graphql_name='aggregationType')
    cvss3_interval = sgqlc.types.Field(IntervalInt, graphql_name='cvss3Interval')
    integral_interval = sgqlc.types.Field(IntervalInt, graphql_name='integralInterval')
    soft_list = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='softList')
    severity_classes = sgqlc.types.Field(sgqlc.types.list_of(SeverityCategories), graphql_name='severityClasses')


class PaginationMalwaresFilterSettings(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('name', 'date_interval', 'aggregation_type', 'expl_list', 'vuln_list', 'severity_classes')
    name = sgqlc.types.Field(String, graphql_name='name')
    date_interval = sgqlc.types.Field(DateTimeIntervalInput, graphql_name='dateInterval')
    aggregation_type = sgqlc.types.Field(AggregationType, graphql_name='aggregationType')
    expl_list = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='explList')
    vuln_list = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='vulnList')
    severity_classes = sgqlc.types.Field(sgqlc.types.list_of(SeverityCategories), graphql_name='severityClasses')


class PaginationOrganizationsFilterSettings(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('name', 'date_interval', 'aggregation_type', 'industry_list', 'severity_classes')
    name = sgqlc.types.Field(String, graphql_name='name')
    date_interval = sgqlc.types.Field(DateTimeIntervalInput, graphql_name='dateInterval')
    aggregation_type = sgqlc.types.Field(AggregationType, graphql_name='aggregationType')
    industry_list = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='industryList')
    severity_classes = sgqlc.types.Field(sgqlc.types.list_of(SeverityCategories), graphql_name='severityClasses')


class PaginationSoftwareNamesFilterSettings(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('name',)
    name = sgqlc.types.Field(String, graphql_name='name')


class PaginationSoftwareVulnsFilterSettings(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('name', 'date_interval', 'aggregation_type', 'soft_types', 'cvss3_interval', 'cwe_list')
    name = sgqlc.types.Field(String, graphql_name='name')
    date_interval = sgqlc.types.Field(DateTimeIntervalInput, graphql_name='dateInterval')
    aggregation_type = sgqlc.types.Field(AggregationType, graphql_name='aggregationType')
    soft_types = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='softTypes')
    cvss3_interval = sgqlc.types.Field(IntervalInt, graphql_name='cvss3Interval')
    cwe_list = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='cweList')


class PaginationVulnerabilityNamesFilterSettings(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('name',)
    name = sgqlc.types.Field(String, graphql_name='name')


class PaginationVulnsFilterSettings(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('name', 'date_interval', 'aggregation_type', 'cvss3_interval', 'integral_interval', 'exploit_amount_interval', 'severity_classes')
    name = sgqlc.types.Field(String, graphql_name='name')
    date_interval = sgqlc.types.Field(DateTimeIntervalInput, graphql_name='dateInterval')
    aggregation_type = sgqlc.types.Field(AggregationType, graphql_name='aggregationType')
    cvss3_interval = sgqlc.types.Field(IntervalInt, graphql_name='cvss3Interval')
    integral_interval = sgqlc.types.Field(IntervalInt, graphql_name='integralInterval')
    exploit_amount_interval = sgqlc.types.Field(IntervalInt, graphql_name='exploitAmountInterval')
    severity_classes = sgqlc.types.Field(sgqlc.types.list_of(SeverityCategories), graphql_name='severityClasses')


class ParameterInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('key', 'value')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')
    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='value')


class PerformSynchronously(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('perform_synchronously',)
    perform_synchronously = sgqlc.types.Field(Boolean, graphql_name='performSynchronously')


class PeriodicJobFilterSettings(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('input_value', 'projects', 'crawlers', 'priorities', 'running_statuses', 'created_by', 'changed_by', 'created_at', 'changed_at', 'next_schedule_time')
    input_value = sgqlc.types.Field(String, graphql_name='inputValue')
    projects = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='projects')
    crawlers = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='crawlers')
    priorities = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(JobPriorityType)), graphql_name='priorities')
    running_statuses = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(PeriodicJobStatus)), graphql_name='runningStatuses')
    created_by = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='createdBy')
    changed_by = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='changedBy')
    created_at = sgqlc.types.Field('TimestampInterval', graphql_name='createdAt')
    changed_at = sgqlc.types.Field('TimestampInterval', graphql_name='changedAt')
    next_schedule_time = sgqlc.types.Field('TimestampInterval', graphql_name='nextScheduleTime')


class PeriodicJobInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('title', 'description', 'crawler_id', 'version_id', 'status', 'priority', 'cron_expression', 'cron_utcoffset_minutes', 'settings', 'args', 'update_on_reload')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    description = sgqlc.types.Field(String, graphql_name='description')
    crawler_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='crawlerId')
    version_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='versionId')
    status = sgqlc.types.Field(PeriodicJobStatus, graphql_name='status')
    priority = sgqlc.types.Field(JobPriorityType, graphql_name='priority')
    cron_expression = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cronExpression')
    cron_utcoffset_minutes = sgqlc.types.Field(Int, graphql_name='cronUTCOffsetMinutes')
    settings = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(KeyValueInputType))), graphql_name='settings')
    args = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(KeyValueInputType))), graphql_name='args')
    update_on_reload = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateOnReload')


class PeriodicTaskFilterSettingsInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('input_value', 'running_statuses', 'task_types', 'access_levels', 'trust_levels', 'creators', 'last_updaters', 'system_registration_date', 'system_update_date', 'next_schedule_time')
    input_value = sgqlc.types.Field(String, graphql_name='inputValue')
    running_statuses = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(RunningStatus)), graphql_name='runningStatuses')
    task_types = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(TaskType)), graphql_name='taskTypes')
    access_levels = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='accessLevels')
    trust_levels = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(TrustLevel)), graphql_name='trustLevels')
    creators = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='creators')
    last_updaters = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='lastUpdaters')
    system_registration_date = sgqlc.types.Field('TimestampIntervalInput', graphql_name='systemRegistrationDate')
    system_update_date = sgqlc.types.Field('TimestampIntervalInput', graphql_name='systemUpdateDate')
    next_schedule_time = sgqlc.types.Field('TimestampIntervalInput', graphql_name='nextScheduleTime')


class PeriodicTaskIdInputInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('periodic_task_id',)
    periodic_task_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='periodicTaskId')


class PipelineConfigFilter(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('in_type', 'system_registration_date', 'system_update_date', 'creator_id', 'last_updater_id', 'description', 'has_transform', 'has_transforms')
    in_type = sgqlc.types.Field(String, graphql_name='inType')
    system_registration_date = sgqlc.types.Field('TimestampInterval', graphql_name='systemRegistrationDate')
    system_update_date = sgqlc.types.Field('TimestampInterval', graphql_name='systemUpdateDate')
    creator_id = sgqlc.types.Field(ID, graphql_name='creatorId')
    last_updater_id = sgqlc.types.Field(ID, graphql_name='lastUpdaterId')
    description = sgqlc.types.Field(String, graphql_name='description')
    has_transform = sgqlc.types.Field(ID, graphql_name='hasTransform')
    has_transforms = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='hasTransforms')


class PipelineConfigInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('id', 'description', 'transforms')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='description')
    transforms = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('PipelineTransformSetupInput'))), graphql_name='transforms')


class PipelineSetupInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('pipeline_config',)
    pipeline_config = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='pipelineConfig')


class PipelineTransformFilter(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('in_type',)
    in_type = sgqlc.types.Field(String, graphql_name='inType')


class PipelineTransformSetupInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('id', 'params')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    params = sgqlc.types.Field(sgqlc.types.non_null(JSON), graphql_name='params')


class PlatformCreationInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('name', 'id', 'platform_type', 'url', 'country', 'language', 'markers', 'params')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    platform_type = sgqlc.types.Field(sgqlc.types.non_null(PlatformType), graphql_name='platformType')
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')
    country = sgqlc.types.Field(String, graphql_name='country')
    language = sgqlc.types.Field(String, graphql_name='language')
    markers = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='markers')
    params = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ParameterInput)), graphql_name='params')


class PlatformFilterSettings(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('search_string', 'id', 'platform_type', 'markers', 'country', 'language', 'creator', 'last_updater', 'registration_date', 'update_date')
    search_string = sgqlc.types.Field(String, graphql_name='searchString')
    id = sgqlc.types.Field(ID, graphql_name='id')
    platform_type = sgqlc.types.Field(PlatformType, graphql_name='platformType')
    markers = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='markers')
    country = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='country')
    language = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='language')
    creator = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='creator')
    last_updater = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='lastUpdater')
    registration_date = sgqlc.types.Field('TimestampInterval', graphql_name='registrationDate')
    update_date = sgqlc.types.Field('TimestampInterval', graphql_name='updateDate')


class PlatformUpdateInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('platform_id', 'name', 'new_id', 'platform_type', 'url', 'country', 'language', 'markers', 'params')
    platform_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='platformId')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    new_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='newId')
    platform_type = sgqlc.types.Field(sgqlc.types.non_null(PlatformType), graphql_name='platformType')
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')
    country = sgqlc.types.Field(String, graphql_name='country')
    language = sgqlc.types.Field(String, graphql_name='language')
    markers = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='markers')
    params = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ParameterInput))), graphql_name='params')


class ProjectFilterSettings(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('input_value', 'name', 'created_by', 'changed_by', 'created_at', 'changed_at')
    input_value = sgqlc.types.Field(String, graphql_name='inputValue')
    name = sgqlc.types.Field(String, graphql_name='name')
    created_by = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='createdBy')
    changed_by = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='changedBy')
    created_at = sgqlc.types.Field('TimestampInterval', graphql_name='createdAt')
    changed_at = sgqlc.types.Field('TimestampInterval', graphql_name='changedAt')


class ProjectInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('title', 'name', 'description', 'eggfile', 'pipfile', 'lockfile', 'settings', 'args')
    title = sgqlc.types.Field(String, graphql_name='title')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    description = sgqlc.types.Field(String, graphql_name='description')
    eggfile = sgqlc.types.Field(String, graphql_name='eggfile')
    pipfile = sgqlc.types.Field(String, graphql_name='pipfile')
    lockfile = sgqlc.types.Field(String, graphql_name='lockfile')
    settings = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(KeyValueInputType))), graphql_name='settings')
    args = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(KeyValueInputType))), graphql_name='args')


class PropertyFilterSettings(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('property_type_id', 'component_id', 'property_type', 'string_filter', 'int_filter', 'double_filter', 'date_time_filter', 'date_time_interval_filter', 'geo_filter')
    property_type_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='propertyTypeId')
    component_id = sgqlc.types.Field(ID, graphql_name='componentId')
    property_type = sgqlc.types.Field(sgqlc.types.non_null(PropLinkOrConcept), graphql_name='propertyType')
    string_filter = sgqlc.types.Field('StringFilter', graphql_name='stringFilter')
    int_filter = sgqlc.types.Field(IntervalInt, graphql_name='intFilter')
    double_filter = sgqlc.types.Field(IntervalDouble, graphql_name='doubleFilter')
    date_time_filter = sgqlc.types.Field(DateTimeIntervalInput, graphql_name='dateTimeFilter')
    date_time_interval_filter = sgqlc.types.Field(DateTimeIntervalPairInput, graphql_name='dateTimeIntervalFilter')
    geo_filter = sgqlc.types.Field(GeoPointWithNameFormInput, graphql_name='geoFilter')


class RegexpToUpdate(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('regexp_to_replace', 'regexp_to_insert')
    regexp_to_replace = sgqlc.types.Field(NERCRegexpInput, graphql_name='regexpToReplace')
    regexp_to_insert = sgqlc.types.Field(NERCRegexpInput, graphql_name='regexpToInsert')


class RelExtModelInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('source_annotation_type', 'target_annotation_type', 'relation_type', 'invert_direction')
    source_annotation_type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='sourceAnnotationType')
    target_annotation_type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='targetAnnotationType')
    relation_type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='relationType')
    invert_direction = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='invertDirection')


class RelatedDocumentFilterSettings(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('document_type', 'publication_date', 'registration_date', 'update_date')
    document_type = sgqlc.types.Field(DocumentType, graphql_name='documentType')
    publication_date = sgqlc.types.Field('TimestampInterval', graphql_name='publicationDate')
    registration_date = sgqlc.types.Field('TimestampInterval', graphql_name='registrationDate')
    update_date = sgqlc.types.Field('TimestampInterval', graphql_name='updateDate')


class RequestFilterSettings(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('input_text', 'interval')
    input_text = sgqlc.types.Field(String, graphql_name='inputText')
    interval = sgqlc.types.Field('TimestampInterval', graphql_name='interval')


class ResearchMapBatchMoveInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('node_move_input',)
    node_move_input = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(NodeMoveInput))), graphql_name='nodeMoveInput')


class ResearchMapBatchUpdateGroupInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('node_ids', 'group_id')
    node_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='nodeIds')
    group_id = sgqlc.types.Field(ID, graphql_name='groupId')


class ResearchMapContentAddInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('documents', 'concepts', 'concept_candidates')
    documents = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(DocumentAddInputInput)), graphql_name='documents')
    concepts = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ConceptAddInputInput)), graphql_name='concepts')
    concept_candidates = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ConceptCandidateAddInputInput)), graphql_name='conceptCandidates')


class ResearchMapContentSelectInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('nodes',)
    nodes = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='nodes')


class ResearchMapContentUpdateInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('nodes',)
    nodes = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='nodes')


class ResearchMapCreationInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('name', 'concepts', 'documents', 'description', 'access_level_id', 'markers')
    name = sgqlc.types.Field(String, graphql_name='name')
    concepts = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='concepts')
    documents = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='documents')
    description = sgqlc.types.Field(String, graphql_name='description')
    access_level_id = sgqlc.types.Field(ID, graphql_name='accessLevelId')
    markers = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='markers')


class ResearchMapFilterSettings(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('name', 'description', 'access_level_id', 'creator', 'last_updater', 'markers', 'creation_date', 'update_date', 'concept_id')
    name = sgqlc.types.Field(String, graphql_name='name')
    description = sgqlc.types.Field(String, graphql_name='description')
    access_level_id = sgqlc.types.Field(ID, graphql_name='accessLevelId')
    creator = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='creator')
    last_updater = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='lastUpdater')
    markers = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='markers')
    creation_date = sgqlc.types.Field('TimestampInterval', graphql_name='creationDate')
    update_date = sgqlc.types.Field('TimestampInterval', graphql_name='updateDate')
    concept_id = sgqlc.types.Field(ID, graphql_name='conceptId')


class ResearchMapUpdateInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('name', 'description', 'access_level_id', 'markers')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    description = sgqlc.types.Field(String, graphql_name='description')
    access_level_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='accessLevelId')
    markers = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='markers')


class RiverEntityFilterSettings(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('date_interval', 'aggregation_type')
    date_interval = sgqlc.types.Field(DateTimeIntervalInput, graphql_name='dateInterval')
    aggregation_type = sgqlc.types.Field(AggregationType, graphql_name='aggregationType')


class SearchElementToUpdate(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('dict', 'regexp')
    dict = sgqlc.types.Field('WordsToUpdate', graphql_name='dict')
    regexp = sgqlc.types.Field(RegexpToUpdate, graphql_name='regexp')


class SearchObjectFilterSettingsInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('target', 'show_search_objects_of_concepts', 'input_value', 'crawlers', 'versions', 'concept_id', 'concept_type_ids', 'created_by', 'changed_by', 'created_at', 'changed_at', 'name')
    target = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(SearchTarget)), graphql_name='target')
    show_search_objects_of_concepts = sgqlc.types.Field(Boolean, graphql_name='showSearchObjectsOfConcepts')
    input_value = sgqlc.types.Field(String, graphql_name='inputValue')
    crawlers = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='crawlers')
    versions = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='versions')
    concept_id = sgqlc.types.Field(ID, graphql_name='conceptId')
    concept_type_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='conceptTypeIds')
    created_by = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='createdBy')
    changed_by = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='changedBy')
    created_at = sgqlc.types.Field('TimestampIntervalInput', graphql_name='createdAt')
    changed_at = sgqlc.types.Field('TimestampIntervalInput', graphql_name='changedAt')
    name = sgqlc.types.Field(String, graphql_name='name')


class SearchObjectsSortingInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('sort', 'direction')
    sort = sgqlc.types.Field(sgqlc.types.non_null(SearchObjectSorting), graphql_name='sort')
    direction = sgqlc.types.Field(sgqlc.types.non_null(SortDirection), graphql_name='direction')


class SearchQueryInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('query', 'concept_id')
    query = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='query')
    concept_id = sgqlc.types.Field(ID, graphql_name='conceptId')


class SoftTypeFilterSettings(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('search',)
    search = sgqlc.types.Field(String, graphql_name='search')


class SoftwareChartFilterSettingsInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('name', 'date_interval', 'soft_types')
    name = sgqlc.types.Field(String, graphql_name='name')
    date_interval = sgqlc.types.Field(DateTimeIntervalInput, graphql_name='dateInterval')
    soft_types = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='softTypes')


class StringFilter(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('str',)
    str = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='str')


class StringLocaleValueInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('value', 'locale')
    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='value')
    locale = sgqlc.types.Field(sgqlc.types.non_null(Locale), graphql_name='locale')


class StringValueInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('value',)
    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='value')


class TaskFilterSettings(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('input_value', 'periodic_task_ids', 'task_ids', 'collection_statuses', 'task_types', 'access_levels', 'trust_levels', 'creators', 'last_updaters', 'system_registration_date', 'system_update_date', 'start_time', 'end_time')
    input_value = sgqlc.types.Field(String, graphql_name='inputValue')
    periodic_task_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='periodicTaskIds')
    task_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Long)), graphql_name='taskIds')
    collection_statuses = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(CollectionStatus)), graphql_name='collectionStatuses')
    task_types = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(TaskType)), graphql_name='taskTypes')
    access_levels = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='accessLevels')
    trust_levels = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(TrustLevel)), graphql_name='trustLevels')
    creators = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='creators')
    last_updaters = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='lastUpdaters')
    system_registration_date = sgqlc.types.Field('TimestampIntervalInput', graphql_name='systemRegistrationDate')
    system_update_date = sgqlc.types.Field('TimestampIntervalInput', graphql_name='systemUpdateDate')
    start_time = sgqlc.types.Field('TimestampIntervalInput', graphql_name='startTime')
    end_time = sgqlc.types.Field('TimestampIntervalInput', graphql_name='endTime')


class TaskPanelInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('filter_id',)
    filter_id = sgqlc.types.Field(ID, graphql_name='filterId')


class TasksFinishedSortInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('sort', 'direction')
    sort = sgqlc.types.Field(sgqlc.types.non_null(TaskFinishedSort), graphql_name='sort')
    direction = sgqlc.types.Field(sgqlc.types.non_null(SortDirection), graphql_name='direction')


class TasksPendingSortInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('sort', 'direction')
    sort = sgqlc.types.Field(sgqlc.types.non_null(TaskPendingSort), graphql_name='sort')
    direction = sgqlc.types.Field(sgqlc.types.non_null(SortDirection), graphql_name='direction')


class TasksRunningSortInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('sort', 'direction')
    sort = sgqlc.types.Field(sgqlc.types.non_null(TaskRunningSort), graphql_name='sort')
    direction = sgqlc.types.Field(sgqlc.types.non_null(SortDirection), graphql_name='direction')


class TasksSort(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('tasks_pending_sort', 'tasks_running_sort', 'tasks_finished_sort')
    tasks_pending_sort = sgqlc.types.Field(sgqlc.types.non_null(TasksPendingSortInput), graphql_name='tasksPendingSort')
    tasks_running_sort = sgqlc.types.Field(sgqlc.types.non_null(TasksRunningSortInput), graphql_name='tasksRunningSort')
    tasks_finished_sort = sgqlc.types.Field(sgqlc.types.non_null(TasksFinishedSortInput), graphql_name='tasksFinishedSort')


class TextBoundingInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('start', 'end', 'node_id')
    start = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='start')
    end = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='end')
    node_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='nodeId')


class TimeInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('hour', 'minute', 'second')
    hour = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='hour')
    minute = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='minute')
    second = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='second')


class TimestampInterval(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('start', 'end')
    start = sgqlc.types.Field(UnixTime, graphql_name='start')
    end = sgqlc.types.Field(UnixTime, graphql_name='end')


class TimestampIntervalInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('start', 'end')
    start = sgqlc.types.Field(UnixTime, graphql_name='start')
    end = sgqlc.types.Field(UnixTime, graphql_name='end')


class TranslationInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('language', 'text')
    language = sgqlc.types.Field(sgqlc.types.non_null(LanguageInput), graphql_name='language')
    text = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='text')


class TypeSearchElementUpdateInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('id', 'elements_type', 'search_element_to_update')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    elements_type = sgqlc.types.Field(sgqlc.types.non_null(ElementType), graphql_name='elementsType')
    search_element_to_update = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(SearchElementToUpdate))), graphql_name='searchElementToUpdate')


class UpdateCommentInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('task_change_id', 'comment')
    task_change_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='taskChangeId')
    comment = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='comment')


class UpdateCurrentUserParams(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('first_name', 'last_name', 'fathers_name', 'email', 'password', 'receive_notifications')
    first_name = sgqlc.types.Field(String, graphql_name='firstName')
    last_name = sgqlc.types.Field(String, graphql_name='lastName')
    fathers_name = sgqlc.types.Field(String, graphql_name='fathersName')
    email = sgqlc.types.Field(String, graphql_name='email')
    password = sgqlc.types.Field(String, graphql_name='password')
    receive_notifications = sgqlc.types.Field(Boolean, graphql_name='receiveNotifications')


class UpdateUserGroupParams(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('name', 'description')
    name = sgqlc.types.Field(String, graphql_name='name')
    description = sgqlc.types.Field(String, graphql_name='description')


class UpdateUserParams(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('first_name', 'last_name', 'fathers_name', 'email', 'access_level_id', 'is_admin', 'redmine_api_key', 'enabled', 'receive_notifications')
    first_name = sgqlc.types.Field(String, graphql_name='firstName')
    last_name = sgqlc.types.Field(String, graphql_name='lastName')
    fathers_name = sgqlc.types.Field(String, graphql_name='fathersName')
    email = sgqlc.types.Field(String, graphql_name='email')
    access_level_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='accessLevelID')
    is_admin = sgqlc.types.Field(Boolean, graphql_name='isAdmin')
    redmine_api_key = sgqlc.types.Field(String, graphql_name='redmineApiKey')
    enabled = sgqlc.types.Field(Boolean, graphql_name='enabled')
    receive_notifications = sgqlc.types.Field(Boolean, graphql_name='receiveNotifications')


class UserAttributeInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('id', 'json_value')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    json_value = sgqlc.types.Field(sgqlc.types.non_null(JSON), graphql_name='jsonValue')


class UserFilterSettings(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('user_id', 'login', 'first_name', 'last_name', 'fathers_name', 'email', 'enabled', 'group_ids', 'creator', 'last_updater', 'creation_date', 'update_date')
    user_id = sgqlc.types.Field(ID, graphql_name='userId')
    login = sgqlc.types.Field(String, graphql_name='login')
    first_name = sgqlc.types.Field(String, graphql_name='firstName')
    last_name = sgqlc.types.Field(String, graphql_name='lastName')
    fathers_name = sgqlc.types.Field(String, graphql_name='fathersName')
    email = sgqlc.types.Field(String, graphql_name='email')
    enabled = sgqlc.types.Field(Boolean, graphql_name='enabled')
    group_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='groupIds')
    creator = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='creator')
    last_updater = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='lastUpdater')
    creation_date = sgqlc.types.Field(TimestampInterval, graphql_name='creationDate')
    update_date = sgqlc.types.Field(TimestampInterval, graphql_name='updateDate')


class UserGroupFilterSettings(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('name', 'description', 'user_ids', 'creator', 'last_updater', 'creation_date', 'update_date')
    name = sgqlc.types.Field(String, graphql_name='name')
    description = sgqlc.types.Field(String, graphql_name='description')
    user_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='userIds')
    creator = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='creator')
    last_updater = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='lastUpdater')
    creation_date = sgqlc.types.Field(TimestampInterval, graphql_name='creationDate')
    update_date = sgqlc.types.Field(TimestampInterval, graphql_name='updateDate')


class UserPipelineTransformFilter(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('in_type',)
    in_type = sgqlc.types.Field(String, graphql_name='inType')


class UserServiceEnvironmentVariableInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('name', 'value')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='value')


class UserServiceInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('mem_limit', 'mem_request', 'cpu_limit', 'cpu_request', 'max_pods', 'environment')
    mem_limit = sgqlc.types.Field(Int, graphql_name='memLimit')
    mem_request = sgqlc.types.Field(Int, graphql_name='memRequest')
    cpu_limit = sgqlc.types.Field(Int, graphql_name='cpuLimit')
    cpu_request = sgqlc.types.Field(Int, graphql_name='cpuRequest')
    max_pods = sgqlc.types.Field(Int, graphql_name='maxPods')
    environment = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(UserServiceEnvironmentVariableInput)), graphql_name='environment')


class ValueInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('string_value_input', 'string_locale_value_input', 'int_value_input', 'double_value_input', 'geo_point_value_input', 'date_time_value_input', 'link_value_input')
    string_value_input = sgqlc.types.Field(StringValueInput, graphql_name='stringValueInput')
    string_locale_value_input = sgqlc.types.Field(StringLocaleValueInput, graphql_name='stringLocaleValueInput')
    int_value_input = sgqlc.types.Field(IntValueInput, graphql_name='intValueInput')
    double_value_input = sgqlc.types.Field(DoubleValueInput, graphql_name='doubleValueInput')
    geo_point_value_input = sgqlc.types.Field(GeoPointInput, graphql_name='geoPointValueInput')
    date_time_value_input = sgqlc.types.Field(DateTimeValueInput, graphql_name='dateTimeValueInput')
    link_value_input = sgqlc.types.Field(LinkValueInput, graphql_name='linkValueInput')


class VersionFilterSettings(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('input_value', 'with_removed_versions')
    input_value = sgqlc.types.Field(String, graphql_name='inputValue')
    with_removed_versions = sgqlc.types.Field(Boolean, graphql_name='withRemovedVersions')


class VersionInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class VulnChartFilterSettingsInput(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('name', 'date_interval', 'integral', 'cvss3')
    name = sgqlc.types.Field(String, graphql_name='name')
    date_interval = sgqlc.types.Field(DateTimeIntervalInput, graphql_name='dateInterval')
    integral = sgqlc.types.Field(IntervalInt, graphql_name='integral')
    cvss3 = sgqlc.types.Field(IntervalInt, graphql_name='cvss3')


class WordsToUpdate(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('word_to_replace', 'word_to_insert')
    word_to_replace = sgqlc.types.Field(String, graphql_name='wordToReplace')
    word_to_insert = sgqlc.types.Field(String, graphql_name='wordToInsert')


class conceptTypeAndEventFilter(sgqlc.types.Input):
    __schema__ = api_schema_new
    __field_names__ = ('full_type', 'is_event')
    full_type = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='fullType')
    is_event = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isEvent')



########################################################################
# Output Objects and Interfaces
########################################################################
class APTGroup(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('apt_group', 'attacks_amount', 'mentions_amount', 'delta', 'history', 'severity_class')
    apt_group = sgqlc.types.Field(sgqlc.types.non_null('Concept'), graphql_name='aptGroup')
    attacks_amount = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='attacksAmount')
    mentions_amount = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='mentionsAmount')
    delta = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='delta')
    history = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('CountDateValue')), graphql_name='history')
    severity_class = sgqlc.types.Field(sgqlc.types.non_null(SeverityCategories), graphql_name='severityClass')


class APTGroupObject(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('apt_group', 'max_history_value', 'history_count', 'next_date')
    apt_group = sgqlc.types.Field(sgqlc.types.non_null(APTGroup), graphql_name='aptGroup')
    max_history_value = sgqlc.types.Field(Int, graphql_name='maxHistoryValue')
    history_count = sgqlc.types.Field(Int, graphql_name='historyCount')
    next_date = sgqlc.types.Field(String, graphql_name='nextDate')


class AccessLevel(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('id', 'name', 'order')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    order = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='order')


class AccessLevelPagination(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('list_access_level', 'total')
    list_access_level = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AccessLevel))), graphql_name='listAccessLevel')
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')


class AccountFacet(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('value', 'count')
    value = sgqlc.types.Field(sgqlc.types.non_null('Account'), graphql_name='value')
    count = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='count')


class AccountPagination(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('list_account', 'total', 'total_platforms')
    list_account = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Account'))), graphql_name='listAccount')
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')
    total_platforms = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalPlatforms')


class AccountStatistics(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('count_doc', 'count_doc_today', 'count_doc_week', 'count_doc_month', 'recall_doc_today', 'recall_doc_week', 'recall_doc_month')
    count_doc = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='countDoc')
    count_doc_today = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='countDocToday')
    count_doc_week = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='countDocWeek')
    count_doc_month = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='countDocMonth')
    recall_doc_today = sgqlc.types.Field(sgqlc.types.non_null(DocumentRecall), graphql_name='recallDocToday')
    recall_doc_week = sgqlc.types.Field(sgqlc.types.non_null(DocumentRecall), graphql_name='recallDocWeek')
    recall_doc_month = sgqlc.types.Field(sgqlc.types.non_null(DocumentRecall), graphql_name='recallDocMonth')


class ActiveMessageList(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('messages', 'total')
    messages = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ActiveMessageStatus'))), graphql_name='messages')
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')


class ActiveMessageStatus(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('id', 'info')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    info = sgqlc.types.Field(sgqlc.types.non_null('MessageInProgress'), graphql_name='info')


class Anchor(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('name', 'params', 'query', 'hash')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    params = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('Parameter')), graphql_name='params')
    query = sgqlc.types.Field(String, graphql_name='query')
    hash = sgqlc.types.Field(String, graphql_name='hash')


class Annotation(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('start', 'end', 'value')
    start = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='start')
    end = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='end')
    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='value')


class ArgsAndSettingsDescription(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('args', 'settings')
    args = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('SettingDescription')), graphql_name='args')
    settings = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('SettingDescription')), graphql_name='settings')


class Attribute(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('id', 'name', 'params_schema')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    params_schema = sgqlc.types.Field(sgqlc.types.non_null('ParamsSchema'), graphql_name='paramsSchema')


class AttributePagination(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('list_attribute', 'total')
    list_attribute = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Attribute))), graphql_name='listAttribute')
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')


class Autocomplete(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('autocomplete',)
    autocomplete = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='autocomplete')


class Chart(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('id', 'description', 'data')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    description = sgqlc.types.Field(sgqlc.types.non_null('ChartDescription'), graphql_name='description')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ChartData'))), graphql_name='data')


class ChartAtomData(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('x', 'y')
    x = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='x')
    y = sgqlc.types.Field(Float, graphql_name='y')


class ChartAtomDataList(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('data',)
    data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ChartAtomData)), graphql_name='data')


class ChartData(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('x', 'y')
    x = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='x')
    y = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='y')


class ChartDescription(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('chart_type', 'target', 'query', 'aggregation_field', 'aggregation_function', 'output_limiter')
    chart_type = sgqlc.types.Field(sgqlc.types.non_null(ChartType), graphql_name='chartType')
    target = sgqlc.types.Field(sgqlc.types.non_null(ChartTarget), graphql_name='target')
    query = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='query')
    aggregation_field = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='aggregationField')
    aggregation_function = sgqlc.types.Field(AggregationFunction, graphql_name='aggregationFunction')
    output_limiter = sgqlc.types.Field(sgqlc.types.non_null('OutputLimiter'), graphql_name='outputLimiter')


class ChartFilters(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('q', 'soft', 'vuln')
    q = sgqlc.types.Field(String, graphql_name='q')
    soft = sgqlc.types.Field('SoftwareChartFilterSettings', graphql_name='soft')
    vuln = sgqlc.types.Field('VulnChartFilterSettings', graphql_name='vuln')


class ChartOutputLimiter(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('maximum_points', 'minimum_number')
    maximum_points = sgqlc.types.Field(Int, graphql_name='maximumPoints')
    minimum_number = sgqlc.types.Field(Int, graphql_name='minimumNumber')


class ChartPanel(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('chart_type', 'target', 'filters', 'aggregation_function', 'aggregation_field', 'grouping_field', 'grouping_step', 'secondary_grouping_field', 'secondary_grouping_step', 'output_limiter', 'data')
    chart_type = sgqlc.types.Field(sgqlc.types.non_null(ChartType), graphql_name='chartType')
    target = sgqlc.types.Field(sgqlc.types.non_null(ChartRTarget), graphql_name='target')
    filters = sgqlc.types.Field(ChartFilters, graphql_name='filters')
    aggregation_function = sgqlc.types.Field(sgqlc.types.non_null(ChartAggregationType), graphql_name='aggregationFunction')
    aggregation_field = sgqlc.types.Field(String, graphql_name='aggregationField')
    grouping_field = sgqlc.types.Field(String, graphql_name='groupingField')
    grouping_step = sgqlc.types.Field(String, graphql_name='groupingStep')
    secondary_grouping_field = sgqlc.types.Field(String, graphql_name='secondaryGroupingField')
    secondary_grouping_step = sgqlc.types.Field(String, graphql_name='secondaryGroupingStep')
    output_limiter = sgqlc.types.Field(ChartOutputLimiter, graphql_name='outputLimiter')
    data = sgqlc.types.Field(sgqlc.types.non_null('ChartRData'), graphql_name='data')


class ChartSeriesData(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('name', 'x', 'y')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    x = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='x')
    y = sgqlc.types.Field(Float, graphql_name='y')


class ChartSeriesDataList(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('data',)
    data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ChartSeriesData)), graphql_name='data')


class CommonStringPagination(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('total', 'list_string')
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')
    list_string = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='listString')


class CompletedOkMessageList(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('messages', 'total')
    messages = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('CompletedOkMessageStatus'))), graphql_name='messages')
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')


class CompletedOkMessageStatus(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('id', 'info')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    info = sgqlc.types.Field(sgqlc.types.non_null('MessageOk'), graphql_name='info')


class CompositeConcept(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('root_concept', 'composite_concept_type', 'id', 'list_concepts', 'paginate_single_widget', 'pagination_concept_mention', 'list_concept_mention')
    root_concept = sgqlc.types.Field(sgqlc.types.non_null('Concept'), graphql_name='rootConcept')
    composite_concept_type = sgqlc.types.Field(sgqlc.types.non_null('CompositeConceptType'), graphql_name='compositeConceptType')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    list_concepts = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Concept'))), graphql_name='listConcepts')
    paginate_single_widget = sgqlc.types.Field(sgqlc.types.non_null('CompositeConceptWidgetRowPagination'), graphql_name='paginateSingleWidget', args=sgqlc.types.ArgDict((
        ('widget_type_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='widgetTypeId', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
))
    )
    pagination_concept_mention = sgqlc.types.Field('ConceptFactPagination', graphql_name='paginationConceptMention', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(DocumentLinkFilterSetting), graphql_name='filterSettings', default=None)),
))
    )
    list_concept_mention = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('ConceptFact')), graphql_name='listConceptMention')


class CompositeConceptPagination(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('list_composite_concept', 'total')
    list_composite_concept = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CompositeConcept))), graphql_name='listCompositeConcept')
    total = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='total')


class CompositeConceptStatistics(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('count_concept_types',)
    count_concept_types = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='countConceptTypes')


class CompositeConceptTypePagination(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('list_composite_concept_type', 'total')
    list_composite_concept_type = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('CompositeConceptType'))), graphql_name='listCompositeConceptType')
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')


class CompositeConceptTypeWidgetTypeColumn(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('id', 'name', 'is_main_properties', 'list_values', 'sort_by_column', 'sort_direction', 'concept_link_types_path', 'property_type', 'metadata', 'link_property_type', 'link_metadata', 'sortable')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    is_main_properties = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isMainProperties')
    list_values = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='listValues')
    sort_by_column = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='sortByColumn')
    sort_direction = sgqlc.types.Field(SortDirection, graphql_name='sortDirection')
    concept_link_types_path = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ConceptLinkTypePath'))), graphql_name='conceptLinkTypesPath')
    property_type = sgqlc.types.Field('ConceptPropertyType', graphql_name='propertyType')
    metadata = sgqlc.types.Field(ConceptTypeMetadata, graphql_name='metadata')
    link_property_type = sgqlc.types.Field('ConceptPropertyType', graphql_name='linkPropertyType')
    link_metadata = sgqlc.types.Field(ConceptTypeLinkMetadata, graphql_name='linkMetadata')
    sortable = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='sortable')


class CompositeConceptTypeWidgetTypePagination(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('list_composite_concept_type_widget', 'total')
    list_composite_concept_type_widget = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('CompositeConceptTypeWidgetType'))), graphql_name='listCompositeConceptTypeWidget')
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')


class CompositeConceptWidgetRowPagination(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('widget_type', 'total', 'rows')
    widget_type = sgqlc.types.Field(sgqlc.types.non_null('CompositeConceptTypeWidgetType'), graphql_name='widgetType')
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')
    rows = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ConceptViewValue'))))))), graphql_name='rows')


class CompositePropertyValueTemplatePagination(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('list_composite_property_value_template', 'total')
    list_composite_property_value_template = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('CompositePropertyValueTemplate'))), graphql_name='listCompositePropertyValueTemplate')
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')


class CompositePropertyValueType(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('id', 'name', 'value_type', 'is_required', 'view')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    value_type = sgqlc.types.Field(sgqlc.types.non_null('ConceptPropertyValueType'), graphql_name='valueType')
    is_required = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isRequired')
    view = sgqlc.types.Field(sgqlc.types.non_null(ComponentView), graphql_name='view')


class CompositeValue(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('list_value',)
    list_value = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('NamedValue'))), graphql_name='listValue')


class ConceptCandidateFactMention(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('concept', 'mention')
    concept = sgqlc.types.Field(sgqlc.types.non_null('ConceptCandidateFact'), graphql_name='concept')
    mention = sgqlc.types.Field(sgqlc.types.non_null('Mention'), graphql_name='mention')


class ConceptFactLink(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('concept_id', 'concept_fact_id', 'status', 'is_implicit', 'concept', 'concept_fact')
    concept_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='conceptId')
    concept_fact_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='conceptFactId')
    status = sgqlc.types.Field(FactStatus, graphql_name='status')
    is_implicit = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isImplicit')
    concept = sgqlc.types.Field(sgqlc.types.non_null('Concept'), graphql_name='concept')
    concept_fact = sgqlc.types.Field(sgqlc.types.non_null('ConceptCandidateFact'), graphql_name='conceptFact')


class ConceptFactPagination(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('total', 'list_concept_fact')
    total = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='total')
    list_concept_fact = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ConceptFact'))), graphql_name='listConceptFact')


class ConceptImplicitLink(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('concept_from_id', 'concept_to_id', 'concept_from', 'concept_to', 'concept_link_type')
    concept_from_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='conceptFromId')
    concept_to_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='conceptToId')
    concept_from = sgqlc.types.Field(sgqlc.types.non_null('Concept'), graphql_name='conceptFrom')
    concept_to = sgqlc.types.Field(sgqlc.types.non_null('Concept'), graphql_name='conceptTo')
    concept_link_type = sgqlc.types.Field(sgqlc.types.non_null('ConceptLinkType'), graphql_name='conceptLinkType')


class ConceptLinkFactPagination(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('total', 'list_concept_link_fact')
    total = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='total')
    list_concept_link_fact = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ConceptLinkFact'))), graphql_name='listConceptLinkFact')


class ConceptLinkPagination(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('total', 'list_concept_link')
    total = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='total')
    list_concept_link = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ConceptLink'))), graphql_name='listConceptLink')


class ConceptLinkTypePagination(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('list_concept_link_type', 'total')
    list_concept_link_type = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ConceptLinkType'))), graphql_name='listConceptLinkType')
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')


class ConceptLinkTypePath(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('link_type', 'fixed')
    link_type = sgqlc.types.Field(sgqlc.types.non_null('ConceptLinkType'), graphql_name='linkType')
    fixed = sgqlc.types.Field(ConceptLinkDirection, graphql_name='fixed')


class ConceptLinkTypeStatistics(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('count_property_type',)
    count_property_type = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='countPropertyType')


class ConceptMention(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('concept', 'mention')
    concept = sgqlc.types.Field(sgqlc.types.non_null('Concept'), graphql_name='concept')
    mention = sgqlc.types.Field(sgqlc.types.non_null('Mention'), graphql_name='mention')


class ConceptPagination(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('total', 'show_total', 'list_concept')
    total = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='total')
    show_total = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='showTotal')
    list_concept = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Concept'))), graphql_name='listConcept')


class ConceptPanel(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('filter_id',)
    filter_id = sgqlc.types.Field(ID, graphql_name='filterId')


class ConceptPropertyPagination(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('total', 'list_concept_property')
    total = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='total')
    list_concept_property = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ConceptProperty'))), graphql_name='listConceptProperty')


class ConceptPropertyTypePagination(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('list_concept_property_type', 'total')
    list_concept_property_type = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ConceptPropertyType'))), graphql_name='listConceptPropertyType')
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')


class ConceptPropertyValueStatistics(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('count_concept_type', 'count_link_type', 'count_dictionary', 'count_regexp')
    count_concept_type = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='countConceptType')
    count_link_type = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='countLinkType')
    count_dictionary = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='countDictionary')
    count_regexp = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='countRegexp')


class ConceptPropertyValueTypePagination(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('list_concept_property_value_type', 'total')
    list_concept_property_value_type = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ConceptPropertyValueType'))), graphql_name='listConceptPropertyValueType')
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')


class ConceptRegistryView(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('columns', 'metrics', 'sorting')
    columns = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ConceptRegistryViewColumn'))), graphql_name='columns')
    metrics = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ConceptRegistryViewMetric'))), graphql_name='metrics')
    sorting = sgqlc.types.Field('ConceptRegistryViewSorting', graphql_name='sorting')


class ConceptRegistryViewColumn(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('column_type',)
    column_type = sgqlc.types.Field(sgqlc.types.non_null(ConceptViewColumnType), graphql_name='columnType')


class ConceptRegistryViewMetric(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('metric_type',)
    metric_type = sgqlc.types.Field(sgqlc.types.non_null(ConceptViewMetricType), graphql_name='metricType')


class ConceptRegistryViewSorting(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('sorting_type', 'sort_direction')
    sorting_type = sgqlc.types.Field(sgqlc.types.non_null(ConceptSorting), graphql_name='sortingType')
    sort_direction = sgqlc.types.Field(sgqlc.types.non_null(SortDirection), graphql_name='sortDirection')


class ConceptStatistics(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('count_properties', 'count_objects', 'count_events', 'count_document_mentions', 'count_document_facts', 'count_potential_documents', 'count_research_maps', 'count_tasks', 'count_concepts', 'count_concepts_and_documents')
    count_properties = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='countProperties')
    count_objects = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='countObjects')
    count_events = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='countEvents')
    count_document_mentions = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='countDocumentMentions')
    count_document_facts = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='countDocumentFacts')
    count_potential_documents = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='countPotentialDocuments')
    count_research_maps = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='countResearchMaps')
    count_tasks = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='countTasks')
    count_concepts = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='countConcepts')
    count_concepts_and_documents = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='countConceptsAndDocuments')


class ConceptSubscriptions(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('subscriptions', 'list_user', 'count_users')
    subscriptions = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ConceptUpdate))), graphql_name='subscriptions')
    list_user = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('User'))), graphql_name='listUser')
    count_users = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='countUsers')


class ConceptTransformConfigList(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('configs', 'total')
    configs = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ConceptTransformConfig'))), graphql_name='configs')
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')


class ConceptTransformResults(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('concepts', 'error')
    concepts = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='concepts')
    error = sgqlc.types.Field(String, graphql_name='error')


class ConceptTransformTaskList(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('tasks', 'total')
    tasks = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ConceptTransformTask'))), graphql_name='tasks')
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')


class ConceptTypePagination(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('list_concept_type', 'total')
    list_concept_type = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ConceptType'))), graphql_name='listConceptType')
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')


class ConceptTypeStatistics(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('count_property_type', 'count_link_type', 'count_dictionary', 'count_regexp')
    count_property_type = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='countPropertyType')
    count_link_type = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='countLinkType')
    count_dictionary = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='countDictionary')
    count_regexp = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='countRegexp')


class ConceptTypeViewPagination(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('list_concept_type_view', 'total')
    list_concept_type_view = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ConceptTypeView'))), graphql_name='listConceptTypeView')
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')


class ConceptView(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('concept', 'rows')
    concept = sgqlc.types.Field(sgqlc.types.non_null('Concept'), graphql_name='concept')
    rows = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ConceptViewValue'))))), graphql_name='rows')


class ConceptViewPagination(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('total', 'list_concept_view')
    total = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='total')
    list_concept_view = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ConceptView))), graphql_name='listConceptView')


class ConceptViewPanel(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('id', 'concept_type_id')
    id = sgqlc.types.Field(ID, graphql_name='id')
    concept_type_id = sgqlc.types.Field(ID, graphql_name='conceptTypeId')


class ConceptWithNeighbors(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('concept', 'num_of_neighbors')
    concept = sgqlc.types.Field(sgqlc.types.non_null('Concept'), graphql_name='concept')
    num_of_neighbors = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='numOfNeighbors')


class ConflictsState(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('user_conflicts', 'group_conflicts')
    user_conflicts = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(Boolean)), graphql_name='userConflicts')
    group_conflicts = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(Boolean)), graphql_name='groupConflicts')


class Coordinates(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('latitude', 'longitude')
    latitude = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='latitude')
    longitude = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='longitude')


class CountDateValue(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('count', 'date')
    count = sgqlc.types.Field(Int, graphql_name='count')
    date = sgqlc.types.Field(String, graphql_name='date')


class CountryPagination(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('list_country', 'total')
    list_country = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='listCountry')
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')


class CrawlerData(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('id', 'title', 'name')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class CrawlerHistogram(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('crawler_name', 'items_scraped_count', 'jobs_count', 'jobs_with_errors_logs')
    crawler_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='crawlerName')
    items_scraped_count = sgqlc.types.Field(Long, graphql_name='itemsScrapedCount')
    jobs_count = sgqlc.types.Field(Int, graphql_name='jobsCount')
    jobs_with_errors_logs = sgqlc.types.Field(Int, graphql_name='jobsWithErrorsLogs')


class CrawlerPagination(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('total', 'list_crawler')
    total = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='total')
    list_crawler = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Crawler'))), graphql_name='listCrawler')


class CrawlerStats(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('items_scraped_count', 'next_schedule_time', 'total_time', 'items_scraped_count_last', 'avg_performance_time', 'last_collection_date')
    items_scraped_count = sgqlc.types.Field(Long, graphql_name='itemsScrapedCount')
    next_schedule_time = sgqlc.types.Field(Long, graphql_name='nextScheduleTime')
    total_time = sgqlc.types.Field(Long, graphql_name='totalTime')
    items_scraped_count_last = sgqlc.types.Field(Long, graphql_name='itemsScrapedCountLast')
    avg_performance_time = sgqlc.types.Field(Long, graphql_name='avgPerformanceTime')
    last_collection_date = sgqlc.types.Field(Long, graphql_name='lastCollectionDate')


class CreateDashboard(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('is_success', 'dashboard')
    is_success = sgqlc.types.Field(Boolean, graphql_name='isSuccess')
    dashboard = sgqlc.types.Field('Dashboard', graphql_name='dashboard')


class CredentialPagination(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('total', 'list_credential')
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')
    list_credential = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Credential'))), graphql_name='listCredential')


class DBConfig(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('url', 'login', 'password', 'db_query_type', 'sql_query', 'target_table', 'file_columns')
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')
    login = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='login')
    password = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='password')
    db_query_type = sgqlc.types.Field(sgqlc.types.non_null(QueryType), graphql_name='dbQueryType')
    sql_query = sgqlc.types.Field(String, graphql_name='sqlQuery')
    target_table = sgqlc.types.Field(String, graphql_name='targetTable')
    file_columns = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('FileQuery'))), graphql_name='fileColumns')


class Dashboard(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('id', 'name', 'description', 'is_main', 'refresh_time', 'editable', 'shared')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='description')
    is_main = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isMain')
    refresh_time = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='refreshTime')
    editable = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='editable')
    shared = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='shared')


class DashboardLayout(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('layout', 'dashboard')
    layout = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('DashboardLayoutItem'))), graphql_name='layout')
    dashboard = sgqlc.types.Field(sgqlc.types.non_null(Dashboard), graphql_name='dashboard')


class DashboardLayoutItem(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('i', 'x', 'y', 'w', 'h', 'min_w', 'max_w', 'min_h', 'max_h', 'static', 'is_draggable', 'is_resizable', 'moved')
    i = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='i')
    x = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='x')
    y = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='y')
    w = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='w')
    h = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='h')
    min_w = sgqlc.types.Field(Int, graphql_name='minW')
    max_w = sgqlc.types.Field(Int, graphql_name='maxW')
    min_h = sgqlc.types.Field(Int, graphql_name='minH')
    max_h = sgqlc.types.Field(Int, graphql_name='maxH')
    static = sgqlc.types.Field(Boolean, graphql_name='static')
    is_draggable = sgqlc.types.Field(Boolean, graphql_name='isDraggable')
    is_resizable = sgqlc.types.Field(Boolean, graphql_name='isResizable')
    moved = sgqlc.types.Field(Boolean, graphql_name='moved')


class DashboardPanel(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('i', 'label', 'data', 'data_type')
    i = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='i')
    label = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='label')
    data = sgqlc.types.Field(sgqlc.types.non_null('DashboardPanelData'), graphql_name='data')
    data_type = sgqlc.types.Field(DashboardPanelType, graphql_name='dataType')


class Dashboards(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('dashboards',)
    dashboards = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Dashboard))), graphql_name='dashboards')


class Date(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('day', 'month', 'year')
    day = sgqlc.types.Field(Int, graphql_name='day')
    month = sgqlc.types.Field(Int, graphql_name='month')
    year = sgqlc.types.Field(Int, graphql_name='year')


class DateHistogramBucket(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('date', 'timestamp', 'doc_count')
    date = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='date')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='timestamp')
    doc_count = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='docCount')


class DateTimeInterval(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('start', 'end')
    start = sgqlc.types.Field('DateTimeValue', graphql_name='start')
    end = sgqlc.types.Field('DateTimeValue', graphql_name='end')


class DateTimeValue(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('date', 'time')
    date = sgqlc.types.Field(sgqlc.types.non_null(Date), graphql_name='date')
    time = sgqlc.types.Field('Time', graphql_name='time')


class DeleteDashboard(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('is_success',)
    is_success = sgqlc.types.Field(Boolean, graphql_name='isSuccess')


class DeployedProject(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('project_id', 'crawlers', 'status', 'update_stats')
    project_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='projectId')
    crawlers = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Crawler'))), graphql_name='crawlers')
    status = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='status')
    update_stats = sgqlc.types.Field(sgqlc.types.non_null('UpdateProjectStats'), graphql_name='updateStats')


class DictValue(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('value',)
    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='value')


class DocSpecificMetadata(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('category', 'last_printed_date', 'last_modified_by', 'created_date', 'comments', 'author', 'document_subject', 'keywords', 'modified_data', 'doc_name')
    category = sgqlc.types.Field(String, graphql_name='category')
    last_printed_date = sgqlc.types.Field(UnixTime, graphql_name='lastPrintedDate')
    last_modified_by = sgqlc.types.Field(String, graphql_name='lastModifiedBy')
    created_date = sgqlc.types.Field(UnixTime, graphql_name='createdDate')
    comments = sgqlc.types.Field(String, graphql_name='comments')
    author = sgqlc.types.Field(String, graphql_name='author')
    document_subject = sgqlc.types.Field(String, graphql_name='documentSubject')
    keywords = sgqlc.types.Field(String, graphql_name='keywords')
    modified_data = sgqlc.types.Field(UnixTime, graphql_name='modifiedData')
    doc_name = sgqlc.types.Field(String, graphql_name='docName')


class DocumentCardView(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('columns', 'metrics')
    columns = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('DocumentCardViewColumn'))), graphql_name='columns')
    metrics = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('DocumentViewMetric'))), graphql_name='metrics')


class DocumentCardViewColumn(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('column_type',)
    column_type = sgqlc.types.Field(sgqlc.types.non_null(DocumentViewColumnType), graphql_name='columnType')


class DocumentFeedPagination(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('list_document_feed', 'total')
    list_document_feed = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('DocumentFeed'))), graphql_name='listDocumentFeed')
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')


class DocumentFromDocumentFeed(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('document', 'is_from_favorites', 'is_from_deleted')
    document = sgqlc.types.Field(sgqlc.types.non_null('Document'), graphql_name='document')
    is_from_favorites = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isFromFavorites')
    is_from_deleted = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isFromDeleted')


class DocumentFromDocumentFeedPagination(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('list_document', 'total', 'show_total')
    list_document = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(DocumentFromDocumentFeed))), graphql_name='listDocument')
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')
    show_total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='showTotal')


class DocumentLink(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('parent_id', 'child_id')
    parent_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='parentId')
    child_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='childId')


class DocumentMetadata(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('file_name', 'size', 'file_type', 'modified_time', 'created_time', 'access_time', 'doc_specific_metadata', 'pdf_specific_metadata', 'image_specific_metadata', 'source', 'language', 'job_id', 'periodic_job_id', 'task_id', 'periodic_task_id', 'platform', 'account')
    file_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='fileName')
    size = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='size')
    file_type = sgqlc.types.Field(String, graphql_name='fileType')
    modified_time = sgqlc.types.Field(sgqlc.types.non_null(UnixTime), graphql_name='modifiedTime')
    created_time = sgqlc.types.Field(sgqlc.types.non_null(UnixTime), graphql_name='createdTime')
    access_time = sgqlc.types.Field(sgqlc.types.non_null(UnixTime), graphql_name='accessTime')
    doc_specific_metadata = sgqlc.types.Field(DocSpecificMetadata, graphql_name='docSpecificMetadata')
    pdf_specific_metadata = sgqlc.types.Field('PdfSpecificMetadataGQL', graphql_name='pdfSpecificMetadata')
    image_specific_metadata = sgqlc.types.Field('ImageSpecificMetadataGQL', graphql_name='imageSpecificMetadata')
    source = sgqlc.types.Field(String, graphql_name='source')
    language = sgqlc.types.Field('Language', graphql_name='language')
    job_id = sgqlc.types.Field(String, graphql_name='jobId')
    periodic_job_id = sgqlc.types.Field(String, graphql_name='periodicJobId')
    task_id = sgqlc.types.Field(String, graphql_name='taskId')
    periodic_task_id = sgqlc.types.Field(String, graphql_name='periodicTaskId')
    platform = sgqlc.types.Field('Platform', graphql_name='platform')
    account = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Account'))), graphql_name='account')


class DocumentPagination(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('list_document', 'total')
    list_document = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Document'))), graphql_name='listDocument')
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')


class DocumentPanel(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('filter_id', 'direction', 'sort_field')
    filter_id = sgqlc.types.Field(ID, graphql_name='filterId')
    direction = sgqlc.types.Field(SortDirection, graphql_name='direction')
    sort_field = sgqlc.types.Field(DocumentSorting, graphql_name='sortField')


class DocumentRegistryView(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('columns', 'metrics', 'sorting')
    columns = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('DocumentRegistryViewColumn'))), graphql_name='columns')
    metrics = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('DocumentViewMetric'))), graphql_name='metrics')
    sorting = sgqlc.types.Field('DocumentRegistryViewSorting', graphql_name='sorting')


class DocumentRegistryViewColumn(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('column_type',)
    column_type = sgqlc.types.Field(sgqlc.types.non_null(DocumentViewColumnType), graphql_name='columnType')


class DocumentRegistryViewSorting(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('sorting_type', 'sort_direction')
    sorting_type = sgqlc.types.Field(sgqlc.types.non_null(DocumentSorting), graphql_name='sortingType')
    sort_direction = sgqlc.types.Field(sgqlc.types.non_null(SortDirection), graphql_name='sortDirection')


class DocumentSubscriptions(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('subscriptions', 'list_user', 'count_users')
    subscriptions = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(DocumentUpdate))), graphql_name='subscriptions')
    list_user = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('User'))), graphql_name='listUser')
    count_users = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='countUsers')


class DocumentViewMetric(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('metric_type',)
    metric_type = sgqlc.types.Field(sgqlc.types.non_null(DocumentViewMetricType), graphql_name='metricType')


class DomainMap(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('list_node', 'list_edge')
    list_node = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('MapNode'))), graphql_name='listNode')
    list_edge = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('MapEdge'))), graphql_name='listEdge')


class DoubleValue(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('value',)
    value = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='value')


class DuplicateMessageList(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('messages', 'total')
    messages = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('DuplicateMessageStatus'))), graphql_name='messages')
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')


class DuplicateMessageStatus(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('id', 'info')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    info = sgqlc.types.Field(sgqlc.types.non_null('MessageDuplicate'), graphql_name='info')


class EmptyPanel(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('stub',)
    stub = sgqlc.types.Field(ID, graphql_name='stub')


class EntityFieldOption(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('label', 'value', 'exclude_chart_types')
    label = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='label')
    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='value')
    exclude_chart_types = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ChartType))), graphql_name='excludeChartTypes')


class Event(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('id', 'target', 'message', 'level', 'anchor', 'is_read', 'params', 'creation_time')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    target = sgqlc.types.Field(sgqlc.types.non_null(EventTarget), graphql_name='target')
    message = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='message')
    level = sgqlc.types.Field(sgqlc.types.non_null(EventLevel), graphql_name='level')
    anchor = sgqlc.types.Field(Anchor, graphql_name='anchor')
    is_read = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isRead')
    params = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Parameter'))), graphql_name='params')
    creation_time = sgqlc.types.Field(sgqlc.types.non_null(UnixTime), graphql_name='creationTime')


class EventPagination(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('list_event', 'total')
    list_event = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Event))), graphql_name='listEvent')
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')


class Exploit(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('exploit', 'publication_date', 'cve', 'cvss3', 'integral', 'software_list', 'mentions_amount', 'delta', 'history', 'severity_class')
    exploit = sgqlc.types.Field(sgqlc.types.non_null('Concept'), graphql_name='exploit')
    publication_date = sgqlc.types.Field(Date, graphql_name='publicationDate')
    cve = sgqlc.types.Field('Concept', graphql_name='cve')
    cvss3 = sgqlc.types.Field(Float, graphql_name='cvss3')
    integral = sgqlc.types.Field(Int, graphql_name='integral')
    software_list = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('Concept')), graphql_name='softwareList')
    mentions_amount = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='mentionsAmount')
    delta = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='delta')
    history = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(CountDateValue)), graphql_name='history')
    severity_class = sgqlc.types.Field(sgqlc.types.non_null(SeverityCategories), graphql_name='severityClass')


class ExploitObject(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('exploit', 'max_history_value', 'history_count', 'next_date')
    exploit = sgqlc.types.Field(sgqlc.types.non_null(Exploit), graphql_name='exploit')
    max_history_value = sgqlc.types.Field(Int, graphql_name='maxHistoryValue')
    history_count = sgqlc.types.Field(Int, graphql_name='historyCount')
    next_date = sgqlc.types.Field(String, graphql_name='nextDate')


class ExportEntity(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('type', 'id')
    type = sgqlc.types.Field(sgqlc.types.non_null(ExportEntityType), graphql_name='type')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class ExportResults(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('file', 'message', 'error')
    file = sgqlc.types.Field(String, graphql_name='file')
    message = sgqlc.types.Field(String, graphql_name='message')
    error = sgqlc.types.Field(String, graphql_name='error')


class ExportTaskList(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('tasks', 'total')
    tasks = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ExportTask'))), graphql_name='tasks')
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')


class ExporterList(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('exporters', 'total')
    exporters = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Exporter'))), graphql_name='exporters')
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')


class ExternalSearchImportConfig(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('access_level', 'task_type', 'topic', 'trust_level', 'config', 'noisy_jobs_count', 'concept_type_id')
    access_level = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='accessLevel')
    task_type = sgqlc.types.Field(sgqlc.types.non_null(TaskType), graphql_name='taskType')
    topic = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='topic')
    trust_level = sgqlc.types.Field(sgqlc.types.non_null(TrustLevel), graphql_name='trustLevel')
    config = sgqlc.types.Field(sgqlc.types.non_null('TaskConfig'), graphql_name='config')
    noisy_jobs_count = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='noisyJobsCount')
    concept_type_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='conceptTypeId')


class ExternalSearchJob(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('id', 'concept', 'search_object', 'job_id', 'collection_status', 'messages_status', 'handled_documents_count', 'creator', 'last_updater', 'system_registration_date', 'system_update_date')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    concept = sgqlc.types.Field('Concept', graphql_name='concept')
    search_object = sgqlc.types.Field(sgqlc.types.non_null('SearchObject'), graphql_name='searchObject')
    job_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='jobId')
    collection_status = sgqlc.types.Field(sgqlc.types.non_null(StepStatus), graphql_name='collectionStatus')
    messages_status = sgqlc.types.Field(sgqlc.types.non_null(StepStatus), graphql_name='messagesStatus')
    handled_documents_count = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='handledDocumentsCount')
    creator = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='creator')
    last_updater = sgqlc.types.Field('User', graphql_name='lastUpdater')
    system_registration_date = sgqlc.types.Field(sgqlc.types.non_null(UnixTime), graphql_name='systemRegistrationDate')
    system_update_date = sgqlc.types.Field(UnixTime, graphql_name='systemUpdateDate')


class ExternalSearchJobConfig(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('crawler', 'version', 'args', 'settings', 'noisy_jobs_count', 'update_on_reload', 'concept_type_id')
    crawler = sgqlc.types.Field(sgqlc.types.non_null('Crawler'), graphql_name='crawler')
    version = sgqlc.types.Field(sgqlc.types.non_null('Version'), graphql_name='version')
    args = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('KeyValue'))), graphql_name='args')
    settings = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('KeyValue'))), graphql_name='settings')
    noisy_jobs_count = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='noisyJobsCount')
    update_on_reload = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateOnReload')
    concept_type_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='conceptTypeId')


class ExternalSearchTask(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('id', 'concept', 'search_object', 'task_id', 'collection_status', 'messages_status', 'handled_documents_count', 'creator', 'last_updater', 'system_registration_date', 'system_update_date')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    concept = sgqlc.types.Field('Concept', graphql_name='concept')
    search_object = sgqlc.types.Field(sgqlc.types.non_null('SearchObject'), graphql_name='searchObject')
    task_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='taskId')
    collection_status = sgqlc.types.Field(sgqlc.types.non_null(StepStatus), graphql_name='collectionStatus')
    messages_status = sgqlc.types.Field(sgqlc.types.non_null(StepStatus), graphql_name='messagesStatus')
    handled_documents_count = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='handledDocumentsCount')
    creator = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='creator')
    last_updater = sgqlc.types.Field('User', graphql_name='lastUpdater')
    system_registration_date = sgqlc.types.Field(sgqlc.types.non_null(UnixTime), graphql_name='systemRegistrationDate')
    system_update_date = sgqlc.types.Field(UnixTime, graphql_name='systemUpdateDate')


class Facet(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('value', 'count')
    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='value')
    count = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='count')


class FactInterface(sgqlc.types.Interface):
    __schema__ = api_schema_new
    __field_names__ = ('id', 'mention', 'system_registration_date', 'system_update_date', 'document')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    mention = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TextBounding'))), graphql_name='mention')
    system_registration_date = sgqlc.types.Field(sgqlc.types.non_null(UnixTime), graphql_name='systemRegistrationDate')
    system_update_date = sgqlc.types.Field(UnixTime, graphql_name='systemUpdateDate')
    document = sgqlc.types.Field(sgqlc.types.non_null('Document'), graphql_name='document')


class FailedMessageList(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('messages', 'total')
    messages = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('MessageStatus'))), graphql_name='messages')
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')


class FileData(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('id', 'file_name')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    file_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='fileName')


class FileQuery(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('name_column', 'data_column', 'is_main_file')
    name_column = sgqlc.types.Field(String, graphql_name='nameColumn')
    data_column = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='dataColumn')
    is_main_file = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isMainFile')


class FileRepositoryConfig(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('url', 'domain', 'login', 'password', 'delete_info_from_resource', 'recursive_traversal')
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')
    domain = sgqlc.types.Field(String, graphql_name='domain')
    login = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='login')
    password = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='password')
    delete_info_from_resource = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteInfoFromResource')
    recursive_traversal = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='recursiveTraversal')


class FilterSettings(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('fs', 'concept_id')
    fs = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='fs')
    concept_id = sgqlc.types.Field(ID, graphql_name='conceptId')


class FlatDocumentStructure(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('text', 'annotations', 'metadata', 'document_id', 'node_id', 'hierarchy_level', 'translated_text', 'id', 'language')
    text = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='text')
    annotations = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Annotation))), graphql_name='annotations')
    metadata = sgqlc.types.Field(sgqlc.types.non_null('ParagraphMetadata'), graphql_name='metadata')
    document_id = sgqlc.types.Field(ID, graphql_name='documentId')
    node_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='nodeId')
    hierarchy_level = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='hierarchyLevel')
    translated_text = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='translatedText')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    language = sgqlc.types.Field('Language', graphql_name='language')


class GeoPointValue(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('point', 'name')
    point = sgqlc.types.Field(Coordinates, graphql_name='point')
    name = sgqlc.types.Field(String, graphql_name='name')


class Group(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('id', 'name', 'x_coordinate', 'y_coordinate', 'collapsed', 'layout')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    x_coordinate = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='xCoordinate')
    y_coordinate = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='yCoordinate')
    collapsed = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='collapsed')
    layout = sgqlc.types.Field(String, graphql_name='layout')


class GroupingStepOption(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('label', 'value')
    label = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='label')
    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='value')


class HLAnnotation(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('start', 'end')
    start = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='start')
    end = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='end')


class HTMLConfig(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('url', 'file_name')
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')
    file_name = sgqlc.types.Field(String, graphql_name='fileName')


class Highlighting(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('highlighting', 'annotations')
    highlighting = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='highlighting')
    annotations = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(HLAnnotation))), graphql_name='annotations')


class Image(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('url', 'thumbnail')
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')
    thumbnail = sgqlc.types.Field(String, graphql_name='thumbnail')


class ImageSpecificMetadataGQL(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('height', 'width', 'orientation')
    height = sgqlc.types.Field(Long, graphql_name='height')
    width = sgqlc.types.Field(Long, graphql_name='width')
    orientation = sgqlc.types.Field(Int, graphql_name='orientation')


class InformationSource(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('id', 'url', 'site_name', 'status', 'periodic_job', 'job', 'crawler', 'error_message')
    id = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='id')
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')
    site_name = sgqlc.types.Field(String, graphql_name='siteName')
    status = sgqlc.types.Field(sgqlc.types.non_null(CollectionStatus), graphql_name='status')
    periodic_job = sgqlc.types.Field('PeriodicJob', graphql_name='periodicJob')
    job = sgqlc.types.Field('Job', graphql_name='job')
    crawler = sgqlc.types.Field('Crawler', graphql_name='crawler')
    error_message = sgqlc.types.Field(String, graphql_name='errorMessage')


class InformationSourceData(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('id', 'url', 'site_name', 'status', 'crawler', 'version_id')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')
    site_name = sgqlc.types.Field(String, graphql_name='siteName')
    status = sgqlc.types.Field(sgqlc.types.non_null(CollectionStatus), graphql_name='status')
    crawler = sgqlc.types.Field(CrawlerData, graphql_name='crawler')
    version_id = sgqlc.types.Field(ID, graphql_name='versionId')


class InformationSourceLoaderStats(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('total_source_count', 'finished_source_count')
    total_source_count = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='totalSourceCount')
    finished_source_count = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='finishedSourceCount')


class IntValue(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('value',)
    value = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='value')


class IntervalIntValue(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('start', 'end')
    start = sgqlc.types.Field(Int, graphql_name='start')
    end = sgqlc.types.Field(Int, graphql_name='end')


class IssueChangePagination(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('total', 'list_issue_change')
    total = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='total')
    list_issue_change = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('IssueChange'))), graphql_name='listIssueChange')


class IssueInfo(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('topic', 'description', 'status', 'priority', 'execution_time_limit', 'markers', 'executor', 'list_concept', 'list_document', 'list_issue')
    topic = sgqlc.types.Field(String, graphql_name='topic')
    description = sgqlc.types.Field(String, graphql_name='description')
    status = sgqlc.types.Field(IssueStatus, graphql_name='status')
    priority = sgqlc.types.Field(IssuePriority, graphql_name='priority')
    execution_time_limit = sgqlc.types.Field(UnixTime, graphql_name='executionTimeLimit')
    markers = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='markers')
    executor = sgqlc.types.Field('User', graphql_name='executor')
    list_concept = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('Concept')), graphql_name='listConcept')
    list_document = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('Document')), graphql_name='listDocument')
    list_issue = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('Issue')), graphql_name='listIssue')


class IssuePagination(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('list_issue', 'total')
    list_issue = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Issue'))), graphql_name='listIssue')
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')


class IssueStatistics(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('count_concept', 'count_doc', 'count_issue')
    count_concept = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='countConcept')
    count_doc = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='countDoc')
    count_issue = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='countIssue')


class Item(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('job_id', 'timestamp', '_uuid', '_url', 'id', 'attachments_num', 'status', 'item')
    job_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='job_id')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(UnixTime), graphql_name='timestamp')
    _uuid = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='_uuid')
    _url = sgqlc.types.Field(String, graphql_name='_url')
    id = sgqlc.types.Field(String, graphql_name='id')
    attachments_num = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='attachmentsNum')
    status = sgqlc.types.Field(sgqlc.types.non_null('MessageStatus'), graphql_name='status')
    item = sgqlc.types.Field(sgqlc.types.non_null(JSON), graphql_name='item')


class ItemsList(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('total', 'items')
    total = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='total')
    items = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Item))), graphql_name='items')


class JobIds(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('job_id', 'task_id', 'periodic_job_id', 'periodic_task_id')
    job_id = sgqlc.types.Field(ID, graphql_name='jobId')
    task_id = sgqlc.types.Field(ID, graphql_name='taskId')
    periodic_job_id = sgqlc.types.Field(ID, graphql_name='periodicJobId')
    periodic_task_id = sgqlc.types.Field(ID, graphql_name='periodicTaskId')


class JobList(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('total', 'list_job')
    total = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='total')
    list_job = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Job'))), graphql_name='listJob')


class JobMetrics(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('job_id', 'metrics')
    job_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='jobId')
    metrics = sgqlc.types.Field(sgqlc.types.non_null('MessageMetrics'), graphql_name='metrics')


class JobPagination(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('total', 'list_job')
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')
    list_job = sgqlc.types.Field(sgqlc.types.non_null('Jobs'), graphql_name='listJob')


class JobStats(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('jobs_count', 'total_time', 'items_scraped_count', 'requests_count', 'errors_count', 'duplicated_request_count', 'jobs_with_errors_logs_count', 'jobs_with_critical_logs_count')
    jobs_count = sgqlc.types.Field(Int, graphql_name='jobsCount')
    total_time = sgqlc.types.Field(Long, graphql_name='totalTime')
    items_scraped_count = sgqlc.types.Field(Long, graphql_name='itemsScrapedCount')
    requests_count = sgqlc.types.Field(Long, graphql_name='requestsCount')
    errors_count = sgqlc.types.Field(Int, graphql_name='errorsCount')
    duplicated_request_count = sgqlc.types.Field(Int, graphql_name='duplicatedRequestCount')
    jobs_with_errors_logs_count = sgqlc.types.Field(Int, graphql_name='jobsWithErrorsLogsCount')
    jobs_with_critical_logs_count = sgqlc.types.Field(Int, graphql_name='jobsWithCriticalLogsCount')


class Jobs(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('pending', 'running', 'finished')
    pending = sgqlc.types.Field(sgqlc.types.non_null(JobList), graphql_name='pending')
    running = sgqlc.types.Field(sgqlc.types.non_null(JobList), graphql_name='running')
    finished = sgqlc.types.Field(sgqlc.types.non_null(JobList), graphql_name='finished')


class KafkaTopicList(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('topics', 'total')
    topics = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('KafkaTopic'))), graphql_name='topics')
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')


class KafkaTopicMetrics(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('messages', 'active_messages', 'pipeline_is_active', 'failed', 'ok', 'ok_cumulative', 'duplicate', 'pending')
    messages = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='messages')
    active_messages = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='activeMessages')
    pipeline_is_active = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='pipelineIsActive')
    failed = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='failed')
    ok = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='ok')
    ok_cumulative = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='okCumulative')
    duplicate = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='duplicate')
    pending = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='pending')


class KeyValue(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('key', 'value')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')
    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='value')


class Language(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('id', 'iso6391', 'iso6392', 'iso6392b', 'iso6392t', 'iso6393', 'iso6395', 'name', 'russian_name', 'english_name', 'target_languages')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    iso6391 = sgqlc.types.Field(String, graphql_name='iso6391')
    iso6392 = sgqlc.types.Field(String, graphql_name='iso6392')
    iso6392b = sgqlc.types.Field(String, graphql_name='iso6392b')
    iso6392t = sgqlc.types.Field(String, graphql_name='iso6392t')
    iso6393 = sgqlc.types.Field(String, graphql_name='iso6393')
    iso6395 = sgqlc.types.Field(String, graphql_name='iso6395')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    russian_name = sgqlc.types.Field(String, graphql_name='russianName')
    english_name = sgqlc.types.Field(String, graphql_name='englishName')
    target_languages = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Language'))), graphql_name='targetLanguages')


class LanguagePagination(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('list_language', 'total')
    list_language = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='listLanguage')
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')


class LinkValue(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('link',)
    link = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='link')


class LocalConfig(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('file_name',)
    file_name = sgqlc.types.Field(String, graphql_name='fileName')


class Log(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('task_id', 'periodic_task_id', 'timestamp', 'level', 'message', 'logger_name', 'stack_trace', 'job_id')
    task_id = sgqlc.types.Field(String, graphql_name='taskId')
    periodic_task_id = sgqlc.types.Field(String, graphql_name='periodicTaskId')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(UnixTime), graphql_name='timestamp')
    level = sgqlc.types.Field(sgqlc.types.non_null(LogLevel), graphql_name='level')
    message = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='message')
    logger_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='loggerName')
    stack_trace = sgqlc.types.Field(String, graphql_name='stackTrace')
    job_id = sgqlc.types.Field(String, graphql_name='jobId')


class Malware(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('malware', 'exploit_list', 'vulnerability_list', 'mentions_amount', 'delta', 'history', 'severity_class')
    malware = sgqlc.types.Field(sgqlc.types.non_null('Concept'), graphql_name='malware')
    exploit_list = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('Concept')), graphql_name='exploitList')
    vulnerability_list = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('Concept')), graphql_name='vulnerabilityList')
    mentions_amount = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='mentionsAmount')
    delta = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='delta')
    history = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(CountDateValue)), graphql_name='history')
    severity_class = sgqlc.types.Field(sgqlc.types.non_null(SeverityCategories), graphql_name='severityClass')


class MalwareObject(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('malware', 'max_history_value', 'history_count', 'next_date')
    malware = sgqlc.types.Field(sgqlc.types.non_null(Malware), graphql_name='malware')
    max_history_value = sgqlc.types.Field(Int, graphql_name='maxHistoryValue')
    history_count = sgqlc.types.Field(Int, graphql_name='historyCount')
    next_date = sgqlc.types.Field(String, graphql_name='nextDate')


class MapEdge(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('from_id', 'to_id', 'link_type', 'id', 'link')
    from_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='fromID')
    to_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='toID')
    link_type = sgqlc.types.Field(sgqlc.types.non_null(MapEdgeType), graphql_name='linkType')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    link = sgqlc.types.Field(sgqlc.types.non_null('EntityLink'), graphql_name='link')


class MapNode(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('id', 'group_id', 'x_coordinate', 'y_coordinate', 'node_type', 'entity')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    group_id = sgqlc.types.Field(ID, graphql_name='groupId')
    x_coordinate = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='xCoordinate')
    y_coordinate = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='yCoordinate')
    node_type = sgqlc.types.Field(sgqlc.types.non_null(MapNodeType), graphql_name='nodeType')
    entity = sgqlc.types.Field(sgqlc.types.non_null('Entity'), graphql_name='entity')


class Markers(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('markers',)
    markers = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='markers')


class Mention(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('id', 'document_id', 'text_bounding', 'verifier', 'system_registration_date', 'system_update_date', 'access_level')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    document_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='documentId')
    text_bounding = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TextBounding'))), graphql_name='textBounding')
    verifier = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='verifier')
    system_registration_date = sgqlc.types.Field(sgqlc.types.non_null(UnixTime), graphql_name='systemRegistrationDate')
    system_update_date = sgqlc.types.Field(UnixTime, graphql_name='systemUpdateDate')
    access_level = sgqlc.types.Field(sgqlc.types.non_null(AccessLevel), graphql_name='accessLevel')


class MergedConcept(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('concept', 'merge_author', 'merge_date')
    concept = sgqlc.types.Field(sgqlc.types.non_null('Concept'), graphql_name='concept')
    merge_author = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='mergeAuthor')
    merge_date = sgqlc.types.Field(sgqlc.types.non_null(UnixTime), graphql_name='mergeDate')


class MergedConceptPagination(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('total', 'list_merged_concept')
    total = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='total')
    list_merged_concept = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(MergedConcept))), graphql_name='listMergedConcept')


class MessageDuplicate(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('create_time', 'start_time', 'finish_time', 'topic', 'result', 'original_id', 'deleted', 'message')
    create_time = sgqlc.types.Field(sgqlc.types.non_null(UnixTime), graphql_name='createTime')
    start_time = sgqlc.types.Field(sgqlc.types.non_null(UnixTime), graphql_name='startTime')
    finish_time = sgqlc.types.Field(sgqlc.types.non_null(UnixTime), graphql_name='finishTime')
    topic = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='topic')
    result = sgqlc.types.Field(String, graphql_name='result')
    original_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='originalId')
    deleted = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleted')
    message = sgqlc.types.Field(sgqlc.types.non_null(JSON), graphql_name='message')


class MessageError(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('description',)
    description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='description')


class MessageFailed(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('create_time', 'start_time', 'finish_time', 'topic', 'stage', 'error', 'deleted', 'duplicate_of', 'message')
    create_time = sgqlc.types.Field(sgqlc.types.non_null(UnixTime), graphql_name='createTime')
    start_time = sgqlc.types.Field(sgqlc.types.non_null(UnixTime), graphql_name='startTime')
    finish_time = sgqlc.types.Field(sgqlc.types.non_null(UnixTime), graphql_name='finishTime')
    topic = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='topic')
    stage = sgqlc.types.Field(sgqlc.types.non_null('PipelineTransformSetup'), graphql_name='stage')
    error = sgqlc.types.Field(sgqlc.types.non_null(MessageError), graphql_name='error')
    deleted = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleted')
    duplicate_of = sgqlc.types.Field(String, graphql_name='duplicateOf')
    message = sgqlc.types.Field(sgqlc.types.non_null(JSON), graphql_name='message')


class MessageInProgress(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('create_time', 'start_time', 'topic', 'stage', 'message')
    create_time = sgqlc.types.Field(sgqlc.types.non_null(UnixTime), graphql_name='createTime')
    start_time = sgqlc.types.Field(sgqlc.types.non_null(UnixTime), graphql_name='startTime')
    topic = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='topic')
    stage = sgqlc.types.Field(sgqlc.types.non_null('PipelineTransformSetup'), graphql_name='stage')
    message = sgqlc.types.Field(sgqlc.types.non_null(JSON), graphql_name='message')


class MessageList(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('messages', 'total')
    messages = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('MessageStatus'))), graphql_name='messages')
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')


class MessageMetrics(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('pending', 'failed', 'ok', 'duplicate')
    pending = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='pending')
    failed = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='failed')
    ok = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='ok')
    duplicate = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='duplicate')


class MessageNotHandled(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('create_time', 'topic', 'not_handled', 'message')
    create_time = sgqlc.types.Field(sgqlc.types.non_null(UnixTime), graphql_name='createTime')
    topic = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='topic')
    not_handled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='notHandled')
    message = sgqlc.types.Field(sgqlc.types.non_null(JSON), graphql_name='message')


class MessageOk(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('create_time', 'start_time', 'finish_time', 'topic', 'result', 'deleted', 'message')
    create_time = sgqlc.types.Field(sgqlc.types.non_null(UnixTime), graphql_name='createTime')
    start_time = sgqlc.types.Field(sgqlc.types.non_null(UnixTime), graphql_name='startTime')
    finish_time = sgqlc.types.Field(sgqlc.types.non_null(UnixTime), graphql_name='finishTime')
    topic = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='topic')
    result = sgqlc.types.Field(String, graphql_name='result')
    deleted = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleted')
    message = sgqlc.types.Field(sgqlc.types.non_null(JSON), graphql_name='message')


class MessageStatus(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('id', 'info')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    info = sgqlc.types.Field(sgqlc.types.non_null('MessageStatusInfo'), graphql_name='info')


class MessageUnknown(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('unknown',)
    unknown = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='unknown')


class Metric(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('job_id', 'timestamp', 'metric')
    job_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='jobId')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(UnixTime), graphql_name='timestamp')
    metric = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='metric')


class Metrics(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('count_objects', 'count_events', 'count_entities', 'count_named_entities', 'count_disambiguated_entities', 'count_links', 'count_research_maps', 'count_child_docs', 'count_tasks', 'count_concepts')
    count_objects = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='countObjects')
    count_events = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='countEvents')
    count_entities = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='countEntities')
    count_named_entities = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='countNamedEntities')
    count_disambiguated_entities = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='countDisambiguatedEntities')
    count_links = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='countLinks')
    count_research_maps = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='countResearchMaps')
    count_child_docs = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='countChildDocs')
    count_tasks = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='countTasks')
    count_concepts = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='countConcepts')


class Mutation(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('update_dashboard_layout', 'update_dashboard_panel', 'create_dashboard', 'update_dashboard', 'delete_dashboard', 'make_thumbnail', 'remove_thumbnail', 'upload_html', 'upload_local', 'upload_report', 'upload_report_from_file', 'add_dbtask', 'add_file_repository_task', 'delete_tasks', 'cancel_tasks', 'add_dbperiodic_task', 'add_file_repository_periodic_task', 'run_periodic_tasks', 'enable_tasks_scheduling', 'disable_tasks_scheduling', 'delete_periodic_tasks', 'update_dbperiodic_task', 'update_file_repository_periodic_task', 'update_crawler', 'update_crawler_settings_arguments_and_state', 'delete_crawler_versions', 'delete_crawlers', 'update_site_map_crawler_body', 'add_credential', 'update_credential', 'delete_credential', 'single_upload', 'add_job', 'delete_job', 'cancel_job', 'add_periodic_job', 'run_periodic_jobs', 'update_enable_jobs_scheduling', 'update_disable_jobs_scheduling', 'delete_periodic_job', 'update_periodic_job', 'update_periodic_job_settings_and_arguments', 'delete_project', 'delete_project_versions', 'add_project', 'update_project', 'update_set_active_project', 'update_remove_active_project', 'update_project_settings_and_arguments', 'add_information_source_loader', 'delete_information_source_loader', 'add_concept', 'add_concept_link', 'update_concept_link', 'add_concept_property', 'add_concept_link_property', 'add_concept_fact', 'delete_concept_fact', 'add_concept_link_property_fact', 'delete_concept_link_property_fact', 'add_concept_property_fact', 'delete_concept_property_fact', 'add_concept_link_fact', 'delete_concept_link_fact', 'update_concept', 'update_concept_avatar', 'update_concept_property', 'delete_concept_property', 'delete_concept_link', 'delete_concept', 'delete_concept_link_property', 'merge_concepts', 'unmerge_concepts', 'delete_fact', 'normalize_value', 'update_concept_subscriptions', 'add_concept_type', 'add_composite_concept_type', 'add_composite_concept_type_widget_type', 'set_concept_type_default_view', 'add_concept_property_type', 'add_concept_link_property_type', 'add_concept_link_type', 'add_concept_property_value_type', 'add_concept_type_view', 'update_concept_type', 'update_composite_concept_type', 'update_composite_concept_type_widget_type', 'update_composite_concept_type_widget_types_order', 'update_concept_property_type', 'update_concept_main_property_type_order', 'update_concept_link_property_type', 'update_concept_link_type', 'update_concept_property_value_type', 'update_concept_type_view', 'delete_concept_type_avatar', 'delete_concept_type', 'delete_composite_concept_type', 'delete_composite_concept_type_widget_type', 'delete_concept_property_type', 'delete_concept_link_property_type', 'delete_concept_link_type', 'delete_concept_property_value_type', 'delete_concept_type_view', 'delete_bulk', 'move_bulk', 'update_type_search_element', 'add_composite_property_value_template', 'update_composite_property_value_template', 'delete_composite_property_value_template', 'add_issue', 'delete_issue', 'add_concept_to_issue', 'add_document_to_issue', 'add_issue_to_issue', 'delete_document_from_issue', 'delete_concept_from_issue', 'delete_issue_from_issue', 'update_issue', 'update_issue_massive', 'add_comment_to_issue', 'update_issue_comment', 'delete_issue_comment', 'update_document', 'update_document_avatar', 'remove_candidate_fact_from_document', 'remove_all_kbfacts_from_document', 'delete_documents', 'add_document_double', 'update_document_node', 'update_document_subscriptions', 'mark_document_as_read', 'mark_document_as_unread', 'delete_research_map', 'bulk_delete_research_map', 'add_research_map', 'add_research_map_from_files', 'update_research_map', 'add_content_on_research_map', 'delete_content_from_research_map', 'batch_move_nodes_on_map', 'batch_update_group_on_map', 'add_top_neighbors_on_map', 'add_concept_fact_neighbors_on_map', 'set_research_map_active', 'find_shortest_path_on_map', 'find_shortest_implicit_path_on_map', 'add_group', 'update_group', 'delete_group', 'unlink_issues', 'add_access_level', 'update_access_level', 'delete_access_level', 'add_template_docx', 'update_markers_bulk', 'add_platform', 'update_platform', 'delete_platform', 'add_account', 'update_account', 'delete_account', 'add_document_feed', 'update_document_feed', 'add_document_to_document_feed_favorites', 'delete_document_from_document_feed_favorites', 'delete_document_from_document_feed', 'restore_document_to_document_feed', 'delete_document_feed', 'update_concept_registry_view', 'update_document_registry_view', 'update_document_card_view', 'add_chart', 'update_chart', 'delete_chart', 'add_pipeline_config', 'copy_pipeline_config', 'import_pipeline_config', 'update_pipeline_config', 'delete_pipeline_config', 'put_kafka_topic', 'update_kafka_topics', 'delete_kafka_topic', 'retry_failed_in_topic', 'retry_failed_message', 'copy_pending_to_kafka', 'reprocess_message', 'reprocess_messages', 'update_exporter', 'add_exporter_task', 'cancel_export_task', 'add_concept_transform_config', 'copy_concept_transform_config', 'update_concept_transform_config', 'update_concept_transform_config_transforms', 'delete_concept_transform_config', 'add_concept_transform_task', 'cancel_concept_transform_task', 'add_user_pipeline_transform', 'update_user_pipeline_transform', 'delete_user_pipeline_transform', 'service_stats', 'add_user', 'update_user_password', 'update_current_user_password', 'update_current_user', 'update_user', 'update_user_attributes', 'delete_user', 'set_kvstore_item', 'delete_kvstore_item', 'add_user_group', 'update_user_group', 'update_user_group_attributes', 'delete_user_group', 'add_user_group_members', 'delete_user_group_members', 'update_event_is_read', 'read_events', 'grant_access', 'revoke_access', 'add_external_search_job', 'delete_external_search_job_by_search_job_ids', 'add_search_query', 'add_filter_settings', 'add_search_query_of_concept', 'add_filter_settings_of_concept', 'add_external_search_object', 'add_external_dbobject', 'add_external_file_repository_object', 'update_search_query', 'update_filter_settings', 'update_search_query_of_concept', 'update_external_search_object', 'update_external_dbobject', 'update_external_file_repository_object', 'update_filter_settings_of_concept', 'delete_search_objects', 'add_noisy_file', 'delete_noisy_file')
    update_dashboard_layout = sgqlc.types.Field('UpdateDashboardLayout', graphql_name='updateDashboardLayout', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(ID, graphql_name='id', default='')),
        ('items', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(DashboardLayoutItemInput))), graphql_name='items', default=None)),
))
    )
    update_dashboard_panel = sgqlc.types.Field('UpdateDashboardPanel', graphql_name='updateDashboardPanel', args=sgqlc.types.ArgDict((
        ('i', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='i', default=None)),
        ('id', sgqlc.types.Arg(ID, graphql_name='id', default='')),
        ('panel', sgqlc.types.Arg(sgqlc.types.non_null(DashboardPanelInput), graphql_name='panel', default=None)),
))
    )
    create_dashboard = sgqlc.types.Field(CreateDashboard, graphql_name='createDashboard', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(DashboardInput), graphql_name='form', default=None)),
))
    )
    update_dashboard = sgqlc.types.Field('UpdateDashboard', graphql_name='updateDashboard', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(DashboardInput), graphql_name='form', default=None)),
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    delete_dashboard = sgqlc.types.Field(DeleteDashboard, graphql_name='deleteDashboard', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    make_thumbnail = sgqlc.types.Field(String, graphql_name='makeThumbnail', args=sgqlc.types.ArgDict((
        ('url', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='url', default=None)),
))
    )
    remove_thumbnail = sgqlc.types.Field(Boolean, graphql_name='removeThumbnail', args=sgqlc.types.ArgDict((
        ('url', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='url', default=None)),
))
    )
    upload_html = sgqlc.types.Field(ID, graphql_name='uploadHtml', args=sgqlc.types.ArgDict((
        ('url', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='url', default=None)),
        ('html', sgqlc.types.Arg(sgqlc.types.non_null(Upload), graphql_name='html', default=None)),
        ('attachments', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AttachmentInput))), graphql_name='attachments', default=None)),
        ('topic', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='topic', default=None)),
))
    )
    upload_local = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='uploadLocal', args=sgqlc.types.ArgDict((
        ('files', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Upload))), graphql_name='files', default=None)),
        ('access_level', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='accessLevel', default=None)),
        ('trust_level', sgqlc.types.Arg(sgqlc.types.non_null(TrustLevel), graphql_name='trustLevel', default=None)),
        ('topic', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='topic', default=None)),
        ('related_concept_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='relatedConceptId', default=None)),
))
    )
    upload_report = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='uploadReport', args=sgqlc.types.ArgDict((
        ('files', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Upload))), graphql_name='files', default=None)),
        ('access_level', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='accessLevel', default=None)),
        ('trust_level', sgqlc.types.Arg(sgqlc.types.non_null(TrustLevel), graphql_name='trustLevel', default=None)),
        ('topic', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='topic', default=None)),
))
    )
    upload_report_from_file = sgqlc.types.Field(ID, graphql_name='uploadReportFromFile', args=sgqlc.types.ArgDict((
        ('file_name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='fileName', default=None)),
        ('access_level', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='accessLevel', default=None)),
        ('trust_level', sgqlc.types.Arg(sgqlc.types.non_null(TrustLevel), graphql_name='trustLevel', default=None)),
        ('topic', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='topic', default=None)),
))
    )
    add_dbtask = sgqlc.types.Field('Task', graphql_name='addDBTask', args=sgqlc.types.ArgDict((
        ('access_level', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='accessLevel', default=None)),
        ('trust_level', sgqlc.types.Arg(sgqlc.types.non_null(TrustLevel), graphql_name='trustLevel', default=None)),
        ('topic', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='topic', default=None)),
        ('task_config', sgqlc.types.Arg(sgqlc.types.non_null(DBConfigInput), graphql_name='taskConfig', default=None)),
))
    )
    add_file_repository_task = sgqlc.types.Field('Task', graphql_name='addFileRepositoryTask', args=sgqlc.types.ArgDict((
        ('access_level', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='accessLevel', default=None)),
        ('trust_level', sgqlc.types.Arg(sgqlc.types.non_null(TrustLevel), graphql_name='trustLevel', default=None)),
        ('topic', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='topic', default=None)),
        ('task_config', sgqlc.types.Arg(sgqlc.types.non_null(FileRepositoryConfigInput), graphql_name='taskConfig', default=None)),
))
    )
    delete_tasks = sgqlc.types.Field('State', graphql_name='deleteTasks', args=sgqlc.types.ArgDict((
        ('task_ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='taskIds', default=None)),
))
    )
    cancel_tasks = sgqlc.types.Field('State', graphql_name='cancelTasks', args=sgqlc.types.ArgDict((
        ('task_ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='taskIds', default=None)),
))
    )
    add_dbperiodic_task = sgqlc.types.Field('PeriodicTask', graphql_name='addDBPeriodicTask', args=sgqlc.types.ArgDict((
        ('title', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='title', default=None)),
        ('description', sgqlc.types.Arg(String, graphql_name='description', default=None)),
        ('access_level', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='accessLevel', default=None)),
        ('trust_level', sgqlc.types.Arg(sgqlc.types.non_null(TrustLevel), graphql_name='trustLevel', default=None)),
        ('topic', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='topic', default=None)),
        ('status', sgqlc.types.Arg(sgqlc.types.non_null(RunningStatus), graphql_name='status', default=None)),
        ('cron_expression', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='cronExpression', default=None)),
        ('cron_utcoffset_minutes', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='cronUTCOffsetMinutes', default=None)),
        ('task_config', sgqlc.types.Arg(sgqlc.types.non_null(DBConfigInput), graphql_name='taskConfig', default=None)),
))
    )
    add_file_repository_periodic_task = sgqlc.types.Field('PeriodicTask', graphql_name='addFileRepositoryPeriodicTask', args=sgqlc.types.ArgDict((
        ('title', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='title', default=None)),
        ('description', sgqlc.types.Arg(String, graphql_name='description', default=None)),
        ('access_level', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='accessLevel', default=None)),
        ('trust_level', sgqlc.types.Arg(sgqlc.types.non_null(TrustLevel), graphql_name='trustLevel', default=None)),
        ('topic', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='topic', default=None)),
        ('status', sgqlc.types.Arg(sgqlc.types.non_null(RunningStatus), graphql_name='status', default=None)),
        ('cron_expression', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='cronExpression', default=None)),
        ('cron_utcoffset_minutes', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='cronUTCOffsetMinutes', default=None)),
        ('task_config', sgqlc.types.Arg(sgqlc.types.non_null(FileRepositoryConfigInput), graphql_name='taskConfig', default=None)),
))
    )
    run_periodic_tasks = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('Task')), graphql_name='runPeriodicTasks', args=sgqlc.types.ArgDict((
        ('periodic_task_ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='periodicTaskIds', default=None)),
))
    )
    enable_tasks_scheduling = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='enableTasksScheduling', args=sgqlc.types.ArgDict((
        ('periodic_task_ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='periodicTaskIds', default=None)),
))
    )
    disable_tasks_scheduling = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='disableTasksScheduling', args=sgqlc.types.ArgDict((
        ('periodic_task_ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='periodicTaskIds', default=None)),
))
    )
    delete_periodic_tasks = sgqlc.types.Field('State', graphql_name='deletePeriodicTasks', args=sgqlc.types.ArgDict((
        ('periodic_task_ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='periodicTaskIds', default=None)),
))
    )
    update_dbperiodic_task = sgqlc.types.Field('PeriodicTask', graphql_name='updateDBPeriodicTask', args=sgqlc.types.ArgDict((
        ('periodic_task_id_input', sgqlc.types.Arg(sgqlc.types.non_null(PeriodicTaskIdInputInput), graphql_name='periodicTaskIdInput', default=None)),
        ('periodic_task_input', sgqlc.types.Arg(sgqlc.types.non_null(AddDBPeriodicTaskInputInput), graphql_name='periodicTaskInput', default=None)),
))
    )
    update_file_repository_periodic_task = sgqlc.types.Field('PeriodicTask', graphql_name='updateFileRepositoryPeriodicTask', args=sgqlc.types.ArgDict((
        ('periodic_task_id_input', sgqlc.types.Arg(sgqlc.types.non_null(PeriodicTaskIdInputInput), graphql_name='periodicTaskIdInput', default=None)),
        ('periodic_task_input', sgqlc.types.Arg(sgqlc.types.non_null(AddFileRepositoryPeriodicTaskInputInput), graphql_name='periodicTaskInput', default=None)),
))
    )
    update_crawler = sgqlc.types.Field(sgqlc.types.non_null('Crawler'), graphql_name='updateCrawler', args=sgqlc.types.ArgDict((
        ('crawler_update_input', sgqlc.types.Arg(sgqlc.types.non_null(CrawlerUpdateInput), graphql_name='crawlerUpdateInput', default=None)),
        ('crawler_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='crawlerId', default=None)),
        ('project_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='projectId', default=None)),
))
    )
    update_crawler_settings_arguments_and_state = sgqlc.types.Field(sgqlc.types.non_null('Crawler'), graphql_name='updateCrawlerSettingsArgumentsAndState', args=sgqlc.types.ArgDict((
        ('crawler_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='crawlerId', default=None)),
        ('settings', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(KeyValueInputType))), graphql_name='settings', default=None)),
        ('args', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(KeyValueInputType))), graphql_name='args', default=None)),
        ('state', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(KeyValueInputType))), graphql_name='state', default=None)),
        ('state_version', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='stateVersion', default=None)),
))
    )
    delete_crawler_versions = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='deleteCrawlerVersions', args=sgqlc.types.ArgDict((
        ('crawler_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='crawlerId', default=None)),
        ('version_ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='versionIds', default=None)),
))
    )
    delete_crawlers = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='deleteCrawlers', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids', default=None)),
))
    )
    update_site_map_crawler_body = sgqlc.types.Field(sgqlc.types.non_null('Crawler'), graphql_name='updateSiteMapCrawlerBody', args=sgqlc.types.ArgDict((
        ('crawler_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='crawlerId', default=None)),
        ('project_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='projectId', default=None)),
        ('json', sgqlc.types.Arg(sgqlc.types.non_null(JSON), graphql_name='json', default=None)),
))
    )
    add_credential = sgqlc.types.Field(sgqlc.types.non_null('Credential'), graphql_name='addCredential', args=sgqlc.types.ArgDict((
        ('credential_input', sgqlc.types.Arg(sgqlc.types.non_null(CredentialInput), graphql_name='credentialInput', default=None)),
))
    )
    update_credential = sgqlc.types.Field(sgqlc.types.non_null('Credential'), graphql_name='updateCredential', args=sgqlc.types.ArgDict((
        ('credential_input', sgqlc.types.Arg(sgqlc.types.non_null(CredentialInput), graphql_name='credentialInput', default=None)),
        ('version', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='version', default=None)),
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    delete_credential = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='deleteCredential', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids', default=None)),
))
    )
    single_upload = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='singleUpload', args=sgqlc.types.ArgDict((
        ('file', sgqlc.types.Arg(Upload, graphql_name='file', default=None)),
))
    )
    add_job = sgqlc.types.Field(sgqlc.types.non_null('Job'), graphql_name='addJob', args=sgqlc.types.ArgDict((
        ('job_input', sgqlc.types.Arg(sgqlc.types.non_null(JobInput), graphql_name='jobInput', default=None)),
))
    )
    delete_job = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='deleteJob', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids', default=None)),
))
    )
    cancel_job = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='cancelJob', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids', default=None)),
))
    )
    add_periodic_job = sgqlc.types.Field(sgqlc.types.non_null('PeriodicJob'), graphql_name='addPeriodicJob', args=sgqlc.types.ArgDict((
        ('periodic_job_input', sgqlc.types.Arg(sgqlc.types.non_null(PeriodicJobInput), graphql_name='periodicJobInput', default=None)),
))
    )
    run_periodic_jobs = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Job'))), graphql_name='runPeriodicJobs', args=sgqlc.types.ArgDict((
        ('periodic_job_ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='periodicJobIds', default=None)),
))
    )
    update_enable_jobs_scheduling = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('PeriodicJob'))), graphql_name='updateEnableJobsScheduling', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids', default=None)),
))
    )
    update_disable_jobs_scheduling = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('PeriodicJob'))), graphql_name='updateDisableJobsScheduling', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids', default=None)),
))
    )
    delete_periodic_job = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='deletePeriodicJob', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids', default=None)),
))
    )
    update_periodic_job = sgqlc.types.Field(sgqlc.types.non_null('PeriodicJob'), graphql_name='updatePeriodicJob', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('periodic_job_input', sgqlc.types.Arg(sgqlc.types.non_null(PeriodicJobInput), graphql_name='periodicJobInput', default=None)),
))
    )
    update_periodic_job_settings_and_arguments = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='updatePeriodicJobSettingsAndArguments', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('settings', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(KeyValueInputType))), graphql_name='settings', default=None)),
        ('args', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(KeyValueInputType))), graphql_name='args', default=None)),
))
    )
    delete_project = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='deleteProject', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids', default=None)),
))
    )
    delete_project_versions = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='deleteProjectVersions', args=sgqlc.types.ArgDict((
        ('project_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='projectId', default=None)),
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids', default=None)),
))
    )
    add_project = sgqlc.types.Field(sgqlc.types.non_null(DeployedProject), graphql_name='addProject', args=sgqlc.types.ArgDict((
        ('project_input', sgqlc.types.Arg(sgqlc.types.non_null(ProjectInput), graphql_name='projectInput', default=None)),
))
    )
    update_project = sgqlc.types.Field(sgqlc.types.non_null(DeployedProject), graphql_name='updateProject', args=sgqlc.types.ArgDict((
        ('project_input', sgqlc.types.Arg(sgqlc.types.non_null(ProjectInput), graphql_name='projectInput', default=None)),
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    update_set_active_project = sgqlc.types.Field(sgqlc.types.non_null('Project'), graphql_name='updateSetActiveProject', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    update_remove_active_project = sgqlc.types.Field(sgqlc.types.non_null('Project'), graphql_name='updateRemoveActiveProject', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    update_project_settings_and_arguments = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='updateProjectSettingsAndArguments', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('settings', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(KeyValueInputType))), graphql_name='settings', default=None)),
        ('args', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(KeyValueInputType))), graphql_name='args', default=None)),
))
    )
    add_information_source_loader = sgqlc.types.Field(sgqlc.types.non_null('InformationSourceLoader'), graphql_name='addInformationSourceLoader', args=sgqlc.types.ArgDict((
        ('information_source_loader_input', sgqlc.types.Arg(sgqlc.types.non_null(InformationSourceLoaderInput), graphql_name='informationSourceLoaderInput', default=None)),
))
    )
    delete_information_source_loader = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='deleteInformationSourceLoader', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids', default=None)),
))
    )
    add_concept = sgqlc.types.Field(sgqlc.types.non_null('Concept'), graphql_name='addConcept', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(ConceptMutationInput), graphql_name='form', default=None)),
        ('performance_control', sgqlc.types.Arg(PerformSynchronously, graphql_name='performanceControl', default=None)),
        ('file', sgqlc.types.Arg(Upload, graphql_name='file', default=None)),
))
    )
    add_concept_link = sgqlc.types.Field(sgqlc.types.non_null('ConceptLink'), graphql_name='addConceptLink', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(ConceptLinkCreationMutationInput), graphql_name='form', default=None)),
        ('performance_control', sgqlc.types.Arg(PerformSynchronously, graphql_name='performanceControl', default=None)),
))
    )
    update_concept_link = sgqlc.types.Field(sgqlc.types.non_null('ConceptLink'), graphql_name='updateConceptLink', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(ConceptLinkUpdateMutationInput), graphql_name='form', default=None)),
))
    )
    add_concept_property = sgqlc.types.Field(sgqlc.types.non_null('ConceptProperty'), graphql_name='addConceptProperty', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(ConceptPropertyCreateInput), graphql_name='form', default=None)),
        ('performance_control', sgqlc.types.Arg(PerformSynchronously, graphql_name='performanceControl', default=None)),
))
    )
    add_concept_link_property = sgqlc.types.Field(sgqlc.types.non_null('ConceptProperty'), graphql_name='addConceptLinkProperty', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(ConceptLinkPropertyInput), graphql_name='form', default=None)),
        ('performance_control', sgqlc.types.Arg(PerformSynchronously, graphql_name='performanceControl', default=None)),
))
    )
    add_concept_fact = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='addConceptFact', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('fact', sgqlc.types.Arg(sgqlc.types.non_null(FactInput), graphql_name='fact', default=None)),
        ('performance_control', sgqlc.types.Arg(PerformSynchronously, graphql_name='performanceControl', default=None)),
))
    )
    delete_concept_fact = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='deleteConceptFact', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    add_concept_link_property_fact = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='addConceptLinkPropertyFact', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('fact', sgqlc.types.Arg(sgqlc.types.non_null(FactInput), graphql_name='fact', default=None)),
        ('performance_control', sgqlc.types.Arg(PerformSynchronously, graphql_name='performanceControl', default=None)),
))
    )
    delete_concept_link_property_fact = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='deleteConceptLinkPropertyFact', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    add_concept_property_fact = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='addConceptPropertyFact', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('fact', sgqlc.types.Arg(sgqlc.types.non_null(FactInput), graphql_name='fact', default=None)),
        ('performance_control', sgqlc.types.Arg(PerformSynchronously, graphql_name='performanceControl', default=None)),
))
    )
    delete_concept_property_fact = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='deleteConceptPropertyFact', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    add_concept_link_fact = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='addConceptLinkFact', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('fact', sgqlc.types.Arg(sgqlc.types.non_null(FactInput), graphql_name='fact', default=None)),
        ('performance_control', sgqlc.types.Arg(PerformSynchronously, graphql_name='performanceControl', default=None)),
))
    )
    delete_concept_link_fact = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='deleteConceptLinkFact', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    update_concept = sgqlc.types.Field(sgqlc.types.non_null('Concept'), graphql_name='updateConcept', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(ConceptUpdateInput), graphql_name='form', default=None)),
        ('performance_control', sgqlc.types.Arg(PerformSynchronously, graphql_name='performanceControl', default=None)),
))
    )
    update_concept_avatar = sgqlc.types.Field(sgqlc.types.non_null('Concept'), graphql_name='updateConceptAvatar', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('document_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='documentId', default=None)),
))
    )
    update_concept_property = sgqlc.types.Field(sgqlc.types.non_null('ConceptProperty'), graphql_name='updateConceptProperty', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(ConceptPropertyUpdateInput), graphql_name='form', default=None)),
))
    )
    delete_concept_property = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='deleteConceptProperty', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    delete_concept_link = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='deleteConceptLink', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    delete_concept = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='deleteConcept', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    delete_concept_link_property = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='deleteConceptLinkProperty', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    merge_concepts = sgqlc.types.Field(sgqlc.types.non_null('Concept'), graphql_name='mergeConcepts', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(ConceptMergeInput), graphql_name='form', default=None)),
))
    )
    unmerge_concepts = sgqlc.types.Field(sgqlc.types.non_null('Concept'), graphql_name='unmergeConcepts', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(ConceptUnmergeInput), graphql_name='form', default=None)),
))
    )
    delete_fact = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='deleteFact', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    normalize_value = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Value'))), graphql_name='normalizeValue', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(NormalizationInput), graphql_name='input', default=None)),
))
    )
    update_concept_subscriptions = sgqlc.types.Field(sgqlc.types.non_null('Concept'), graphql_name='updateConceptSubscriptions', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('events', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ConceptUpdate))), graphql_name='events', default=None)),
))
    )
    add_concept_type = sgqlc.types.Field(sgqlc.types.non_null('ConceptType'), graphql_name='addConceptType', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(ConceptTypeCreationInput), graphql_name='form', default=None)),
        ('file', sgqlc.types.Arg(Upload, graphql_name='file', default=None)),
))
    )
    add_composite_concept_type = sgqlc.types.Field(sgqlc.types.non_null('CompositeConceptType'), graphql_name='addCompositeConceptType', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(CompositeConceptTypeCreationInput), graphql_name='form', default=None)),
))
    )
    add_composite_concept_type_widget_type = sgqlc.types.Field(sgqlc.types.non_null('CompositeConceptTypeWidgetType'), graphql_name='addCompositeConceptTypeWidgetType', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(CompositeConceptTypeWidgetTypeCreationInput), graphql_name='form', default=None)),
))
    )
    set_concept_type_default_view = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='setConceptTypeDefaultView', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(CompositeConceptTypeViewInput), graphql_name='form', default=None)),
))
    )
    add_concept_property_type = sgqlc.types.Field(sgqlc.types.non_null('ConceptPropertyType'), graphql_name='addConceptPropertyType', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(ConceptPropertyTypeCreationInput), graphql_name='form', default=None)),
))
    )
    add_concept_link_property_type = sgqlc.types.Field(sgqlc.types.non_null('ConceptPropertyType'), graphql_name='addConceptLinkPropertyType', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(ConceptLinkPropertyTypeCreationInput), graphql_name='form', default=None)),
))
    )
    add_concept_link_type = sgqlc.types.Field(sgqlc.types.non_null('ConceptLinkType'), graphql_name='addConceptLinkType', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(ConceptLinkTypeCreationInput), graphql_name='form', default=None)),
))
    )
    add_concept_property_value_type = sgqlc.types.Field(sgqlc.types.non_null('ConceptPropertyValueType'), graphql_name='addConceptPropertyValueType', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(ConceptPropertyValueTypeCreationInput), graphql_name='form', default=None)),
))
    )
    add_concept_type_view = sgqlc.types.Field(sgqlc.types.non_null('ConceptTypeView'), graphql_name='addConceptTypeView', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(ConceptTypeViewCreationInput), graphql_name='form', default=None)),
))
    )
    update_concept_type = sgqlc.types.Field(sgqlc.types.non_null('ConceptType'), graphql_name='updateConceptType', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(ConceptTypeUpdateInput), graphql_name='form', default=None)),
        ('file', sgqlc.types.Arg(Upload, graphql_name='file', default=None)),
))
    )
    update_composite_concept_type = sgqlc.types.Field(sgqlc.types.non_null('CompositeConceptType'), graphql_name='updateCompositeConceptType', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(CompositeConceptTypeUpdateInput), graphql_name='form', default=None)),
))
    )
    update_composite_concept_type_widget_type = sgqlc.types.Field(sgqlc.types.non_null('CompositeConceptTypeWidgetType'), graphql_name='updateCompositeConceptTypeWidgetType', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(CompositeConceptTypeWidgetTypeUpdateInput), graphql_name='form', default=None)),
))
    )
    update_composite_concept_type_widget_types_order = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='updateCompositeConceptTypeWidgetTypesOrder', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(CompositeConceptTypeWidgetTypeUpdateOrderInput), graphql_name='form', default=None)),
))
    )
    update_concept_property_type = sgqlc.types.Field(sgqlc.types.non_null('ConceptPropertyType'), graphql_name='updateConceptPropertyType', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(ConceptPropertyTypeUpdateInput), graphql_name='form', default=None)),
))
    )
    update_concept_main_property_type_order = sgqlc.types.Field(sgqlc.types.non_null('ConceptType'), graphql_name='updateConceptMainPropertyTypeOrder', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(InterestObjectMainPropertiesOrderUpdateInput), graphql_name='form', default=None)),
))
    )
    update_concept_link_property_type = sgqlc.types.Field(sgqlc.types.non_null('ConceptPropertyType'), graphql_name='updateConceptLinkPropertyType', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(ConceptLinkPropertyTypeUpdateInput), graphql_name='form', default=None)),
))
    )
    update_concept_link_type = sgqlc.types.Field(sgqlc.types.non_null('ConceptLinkType'), graphql_name='updateConceptLinkType', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(ConceptLinkTypeUpdateInput), graphql_name='form', default=None)),
))
    )
    update_concept_property_value_type = sgqlc.types.Field(sgqlc.types.non_null('ConceptPropertyValueType'), graphql_name='updateConceptPropertyValueType', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(ConceptPropertyValueTypeUpdateInput), graphql_name='form', default=None)),
))
    )
    update_concept_type_view = sgqlc.types.Field(sgqlc.types.non_null('ConceptTypeView'), graphql_name='updateConceptTypeView', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(ConceptTypeViewUpdateInput), graphql_name='form', default=None)),
))
    )
    delete_concept_type_avatar = sgqlc.types.Field(sgqlc.types.non_null('ConceptType'), graphql_name='deleteConceptTypeAvatar', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    delete_concept_type = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='deleteConceptType', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    delete_composite_concept_type = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='deleteCompositeConceptType', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    delete_composite_concept_type_widget_type = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='deleteCompositeConceptTypeWidgetType', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    delete_concept_property_type = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='deleteConceptPropertyType', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    delete_concept_link_property_type = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='deleteConceptLinkPropertyType', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    delete_concept_link_type = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='deleteConceptLinkType', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    delete_concept_property_value_type = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='deleteConceptPropertyValueType', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    delete_concept_type_view = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='deleteConceptTypeView', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    delete_bulk = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('State')), graphql_name='deleteBulk', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids', default=None)),
))
    )
    move_bulk = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ConceptType'))), graphql_name='moveBulk', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids', default=None)),
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Coordinate))), graphql_name='form', default=None)),
))
    )
    update_type_search_element = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='updateTypeSearchElement', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(TypeSearchElementUpdateInput), graphql_name='form', default=None)),
))
    )
    add_composite_property_value_template = sgqlc.types.Field(sgqlc.types.non_null('CompositePropertyValueTemplate'), graphql_name='addCompositePropertyValueTemplate', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(CompositePropertyValueTemplateCreateInput), graphql_name='form', default=None)),
))
    )
    update_composite_property_value_template = sgqlc.types.Field(sgqlc.types.non_null('CompositePropertyValueTemplate'), graphql_name='updateCompositePropertyValueTemplate', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(CompositePropertyValueTemplateCreateInput), graphql_name='form', default=None)),
))
    )
    delete_composite_property_value_template = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='deleteCompositePropertyValueTemplate', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    add_issue = sgqlc.types.Field(sgqlc.types.non_null('Issue'), graphql_name='addIssue', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(IssueCreationInput), graphql_name='form', default=None)),
))
    )
    delete_issue = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='deleteIssue', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    add_concept_to_issue = sgqlc.types.Field(sgqlc.types.non_null('Issue'), graphql_name='addConceptToIssue', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(Concept2IssueInput), graphql_name='form', default=None)),
))
    )
    add_document_to_issue = sgqlc.types.Field(sgqlc.types.non_null('Issue'), graphql_name='addDocumentToIssue', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(Document2IssueInput), graphql_name='form', default=None)),
))
    )
    add_issue_to_issue = sgqlc.types.Field(sgqlc.types.non_null('Issue'), graphql_name='addIssueToIssue', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(Issue2TaskInput), graphql_name='form', default=None)),
))
    )
    delete_document_from_issue = sgqlc.types.Field(sgqlc.types.non_null('Issue'), graphql_name='deleteDocumentFromIssue', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(Document2IssueInput), graphql_name='form', default=None)),
))
    )
    delete_concept_from_issue = sgqlc.types.Field(sgqlc.types.non_null('Issue'), graphql_name='deleteConceptFromIssue', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(Concept2IssueInput), graphql_name='form', default=None)),
))
    )
    delete_issue_from_issue = sgqlc.types.Field(sgqlc.types.non_null('Issue'), graphql_name='deleteIssueFromIssue', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(Issue2TaskInput), graphql_name='form', default=None)),
))
    )
    update_issue = sgqlc.types.Field(sgqlc.types.non_null('Issue'), graphql_name='updateIssue', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(IssueEditFieldsInput), graphql_name='form', default=None)),
))
    )
    update_issue_massive = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='updateIssueMassive', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(MassUpdateIssueInput), graphql_name='form', default=None)),
))
    )
    add_comment_to_issue = sgqlc.types.Field(sgqlc.types.non_null('IssueChange'), graphql_name='addCommentToIssue', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(Comment2IssueInput), graphql_name='form', default=None)),
))
    )
    update_issue_comment = sgqlc.types.Field(sgqlc.types.non_null('IssueChange'), graphql_name='updateIssueComment', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(UpdateCommentInput), graphql_name='form', default=None)),
))
    )
    delete_issue_comment = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='deleteIssueComment', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    update_document = sgqlc.types.Field(sgqlc.types.non_null('Document'), graphql_name='updateDocument', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(DocumentUpdateInput), graphql_name='form', default=None)),
))
    )
    update_document_avatar = sgqlc.types.Field(sgqlc.types.non_null('Document'), graphql_name='updateDocumentAvatar', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(DocumentAvatarUpdateInput), graphql_name='form', default=None)),
))
    )
    remove_candidate_fact_from_document = sgqlc.types.Field(sgqlc.types.non_null('Document'), graphql_name='removeCandidateFactFromDocument', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(DocumentDeleteCandidateFactInput), graphql_name='form', default=None)),
))
    )
    remove_all_kbfacts_from_document = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='removeAllKBFactsFromDocument', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(DocumentAllKBFactsRemoveInput), graphql_name='form', default=None)),
))
    )
    delete_documents = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='deleteDocuments', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids', default=None)),
))
    )
    add_document_double = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='addDocumentDouble', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(DocumentDoubleCreationInput), graphql_name='form', default=None)),
))
    )
    update_document_node = sgqlc.types.Field(sgqlc.types.non_null('Document'), graphql_name='updateDocumentNode', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(DocumentNodeUpdateInput), graphql_name='form', default=None)),
))
    )
    update_document_subscriptions = sgqlc.types.Field(sgqlc.types.non_null('Document'), graphql_name='updateDocumentSubscriptions', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('events', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(DocumentUpdate))), graphql_name='events', default=None)),
))
    )
    mark_document_as_read = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='markDocumentAsRead', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    mark_document_as_unread = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='markDocumentAsUnread', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    delete_research_map = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='deleteResearchMap', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    bulk_delete_research_map = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='bulkDeleteResearchMap', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids', default=None)),
))
    )
    add_research_map = sgqlc.types.Field(sgqlc.types.non_null('ResearchMap'), graphql_name='addResearchMap', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(ResearchMapCreationInput), graphql_name='form', default=None)),
))
    )
    add_research_map_from_files = sgqlc.types.Field(sgqlc.types.non_null('ResearchMapFromFilesType'), graphql_name='addResearchMapFromFiles', args=sgqlc.types.ArgDict((
        ('files', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(Upload)), graphql_name='files', default=None)),
))
    )
    update_research_map = sgqlc.types.Field(sgqlc.types.non_null('ResearchMap'), graphql_name='updateResearchMap', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(ResearchMapUpdateInput), graphql_name='form', default=None)),
))
    )
    add_content_on_research_map = sgqlc.types.Field(sgqlc.types.non_null('ResearchMap'), graphql_name='addContentOnResearchMap', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(ResearchMapContentAddInput), graphql_name='form', default=None)),
))
    )
    delete_content_from_research_map = sgqlc.types.Field(sgqlc.types.non_null('ResearchMap'), graphql_name='deleteContentFromResearchMap', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(ResearchMapContentUpdateInput), graphql_name='form', default=None)),
))
    )
    batch_move_nodes_on_map = sgqlc.types.Field(sgqlc.types.non_null('ResearchMap'), graphql_name='batchMoveNodesOnMap', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(ResearchMapBatchMoveInput), graphql_name='form', default=None)),
))
    )
    batch_update_group_on_map = sgqlc.types.Field(sgqlc.types.non_null('ResearchMap'), graphql_name='batchUpdateGroupOnMap', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(ResearchMapBatchUpdateGroupInput), graphql_name='form', default=None)),
))
    )
    add_top_neighbors_on_map = sgqlc.types.Field(sgqlc.types.non_null('ResearchMap'), graphql_name='addTopNeighborsOnMap', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('quantity', sgqlc.types.Arg(Int, graphql_name='quantity', default=10)),
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(ResearchMapContentSelectInput), graphql_name='form', default=None)),
))
    )
    add_concept_fact_neighbors_on_map = sgqlc.types.Field(sgqlc.types.non_null('ResearchMap'), graphql_name='addConceptFactNeighborsOnMap', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('concept_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='conceptId', default=None)),
))
    )
    set_research_map_active = sgqlc.types.Field(sgqlc.types.non_null('ResearchMap'), graphql_name='setResearchMapActive', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    find_shortest_path_on_map = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='findShortestPathOnMap', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('concept_node_ids', sgqlc.types.Arg(sgqlc.types.non_null(ConceptAddImplicitLinkInput), graphql_name='conceptNodeIds', default=None)),
))
    )
    find_shortest_implicit_path_on_map = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='findShortestImplicitPathOnMap', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('concept_node_ids', sgqlc.types.Arg(sgqlc.types.non_null(ConceptAddImplicitLinkInput), graphql_name='conceptNodeIds', default=None)),
))
    )
    add_group = sgqlc.types.Field(sgqlc.types.non_null(Group), graphql_name='addGroup', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(GroupCreationInput), graphql_name='form', default=None)),
))
    )
    update_group = sgqlc.types.Field(sgqlc.types.non_null(Group), graphql_name='updateGroup', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(GroupUpdateInput), graphql_name='form', default=None)),
))
    )
    delete_group = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='deleteGroup', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    unlink_issues = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='unlinkIssues')
    add_access_level = sgqlc.types.Field(sgqlc.types.non_null(AccessLevel), graphql_name='addAccessLevel', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(AccessLevelCreationInput), graphql_name='form', default=None)),
))
    )
    update_access_level = sgqlc.types.Field(sgqlc.types.non_null(AccessLevel), graphql_name='updateAccessLevel', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(AccessLevelUpdateInput), graphql_name='form', default=None)),
))
    )
    delete_access_level = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='deleteAccessLevel', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    add_template_docx = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='addTemplateDocx', args=sgqlc.types.ArgDict((
        ('file', sgqlc.types.Arg(Upload, graphql_name='file', default=None)),
))
    )
    update_markers_bulk = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='updateMarkersBulk', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(BulkMarkersUpdateInput), graphql_name='form', default=None)),
))
    )
    add_platform = sgqlc.types.Field(sgqlc.types.non_null('Platform'), graphql_name='addPlatform', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(PlatformCreationInput), graphql_name='form', default=None)),
        ('file', sgqlc.types.Arg(Upload, graphql_name='file', default=None)),
))
    )
    update_platform = sgqlc.types.Field(sgqlc.types.non_null('Platform'), graphql_name='updatePlatform', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(PlatformUpdateInput), graphql_name='form', default=None)),
        ('file', sgqlc.types.Arg(Upload, graphql_name='file', default=None)),
))
    )
    delete_platform = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='deletePlatform', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    add_account = sgqlc.types.Field(sgqlc.types.non_null('Account'), graphql_name='addAccount', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(AccountCreationInput), graphql_name='form', default=None)),
        ('file', sgqlc.types.Arg(Upload, graphql_name='file', default=None)),
))
    )
    update_account = sgqlc.types.Field(sgqlc.types.non_null('Account'), graphql_name='updateAccount', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(AccountUpdateInput), graphql_name='form', default=None)),
        ('file', sgqlc.types.Arg(Upload, graphql_name='file', default=None)),
))
    )
    delete_account = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='deleteAccount', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    add_document_feed = sgqlc.types.Field(sgqlc.types.non_null('DocumentFeed'), graphql_name='addDocumentFeed', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(DocumentFeedCreationInput), graphql_name='form', default=None)),
))
    )
    update_document_feed = sgqlc.types.Field(sgqlc.types.non_null('DocumentFeed'), graphql_name='updateDocumentFeed', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(DocumentFeedUpdateInput), graphql_name='form', default=None)),
))
    )
    add_document_to_document_feed_favorites = sgqlc.types.Field(sgqlc.types.non_null('DocumentFeed'), graphql_name='addDocumentToDocumentFeedFavorites', args=sgqlc.types.ArgDict((
        ('document_feed_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='documentFeedId', default=None)),
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(DocumentFeedUpdateDocumentsInput), graphql_name='form', default=None)),
))
    )
    delete_document_from_document_feed_favorites = sgqlc.types.Field(sgqlc.types.non_null('DocumentFeed'), graphql_name='deleteDocumentFromDocumentFeedFavorites', args=sgqlc.types.ArgDict((
        ('document_feed_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='documentFeedId', default=None)),
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(DocumentFeedUpdateDocumentsInput), graphql_name='form', default=None)),
))
    )
    delete_document_from_document_feed = sgqlc.types.Field(sgqlc.types.non_null('DocumentFeed'), graphql_name='deleteDocumentFromDocumentFeed', args=sgqlc.types.ArgDict((
        ('document_feed_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='documentFeedId', default=None)),
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(DocumentFeedUpdateDocumentsInput), graphql_name='form', default=None)),
))
    )
    restore_document_to_document_feed = sgqlc.types.Field(sgqlc.types.non_null('DocumentFeed'), graphql_name='restoreDocumentToDocumentFeed', args=sgqlc.types.ArgDict((
        ('document_feed_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='documentFeedId', default=None)),
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(DocumentFeedUpdateDocumentsInput), graphql_name='form', default=None)),
))
    )
    delete_document_feed = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='deleteDocumentFeed', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    update_concept_registry_view = sgqlc.types.Field(sgqlc.types.non_null(ConceptRegistryView), graphql_name='updateConceptRegistryView', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(ConceptRegistryViewInput), graphql_name='form', default=None)),
))
    )
    update_document_registry_view = sgqlc.types.Field(sgqlc.types.non_null(DocumentRegistryView), graphql_name='updateDocumentRegistryView', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(DocumentRegistryViewInput), graphql_name='form', default=None)),
))
    )
    update_document_card_view = sgqlc.types.Field(sgqlc.types.non_null(DocumentCardView), graphql_name='updateDocumentCardView', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(DocumentCardViewInput), graphql_name='form', default=None)),
))
    )
    add_chart = sgqlc.types.Field(sgqlc.types.non_null(Chart), graphql_name='addChart', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(ChartDescriptionInput), graphql_name='form', default=None)),
))
    )
    update_chart = sgqlc.types.Field(sgqlc.types.non_null(Chart), graphql_name='updateChart', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(ChartDescriptionInput), graphql_name='form', default=None)),
))
    )
    delete_chart = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='deleteChart', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    add_pipeline_config = sgqlc.types.Field(sgqlc.types.non_null('PipelineConfig'), graphql_name='addPipelineConfig', args=sgqlc.types.ArgDict((
        ('description', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='description', default=None)),
        ('transforms', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(PipelineTransformSetupInput))), graphql_name='transforms', default=None)),
))
    )
    copy_pipeline_config = sgqlc.types.Field(sgqlc.types.non_null('PipelineConfig'), graphql_name='copyPipelineConfig', args=sgqlc.types.ArgDict((
        ('source_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='sourceId', default=None)),
        ('description', sgqlc.types.Arg(String, graphql_name='description', default=None)),
))
    )
    import_pipeline_config = sgqlc.types.Field(sgqlc.types.non_null('PipelineConfig'), graphql_name='importPipelineConfig', args=sgqlc.types.ArgDict((
        ('export', sgqlc.types.Arg(sgqlc.types.non_null(Upload), graphql_name='export', default=None)),
))
    )
    update_pipeline_config = sgqlc.types.Field(sgqlc.types.non_null('PipelineConfig'), graphql_name='updatePipelineConfig', args=sgqlc.types.ArgDict((
        ('pipeline_config', sgqlc.types.Arg(sgqlc.types.non_null(PipelineConfigInput), graphql_name='pipelineConfig', default=None)),
))
    )
    delete_pipeline_config = sgqlc.types.Field(sgqlc.types.non_null('PipelineConfig'), graphql_name='deletePipelineConfig', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    put_kafka_topic = sgqlc.types.Field(sgqlc.types.non_null('KafkaTopic'), graphql_name='putKafkaTopic', args=sgqlc.types.ArgDict((
        ('topic', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='topic', default=None)),
        ('description', sgqlc.types.Arg(String, graphql_name='description', default=None)),
        ('pipeline', sgqlc.types.Arg(PipelineSetupInput, graphql_name='pipeline', default=None)),
        ('priority', sgqlc.types.Arg(Int, graphql_name='priority', default=0)),
        ('request_timeout_ms', sgqlc.types.Arg(Int, graphql_name='requestTimeoutMs', default=None)),
        ('move_to_on_timeout', sgqlc.types.Arg(String, graphql_name='moveToOnTimeout', default=None)),
))
    )
    update_kafka_topics = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='updateKafkaTopics', args=sgqlc.types.ArgDict((
        ('topics', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='topics', default=None)),
        ('update', sgqlc.types.Arg(sgqlc.types.non_null(KafkaTopicUpdate), graphql_name='update', default=None)),
))
    )
    delete_kafka_topic = sgqlc.types.Field(sgqlc.types.non_null('KafkaTopic'), graphql_name='deleteKafkaTopic', args=sgqlc.types.ArgDict((
        ('topic', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='topic', default=None)),
))
    )
    retry_failed_in_topic = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='retryFailedInTopic', args=sgqlc.types.ArgDict((
        ('topic', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='topic', default=None)),
))
    )
    retry_failed_message = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='retryFailedMessage', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    copy_pending_to_kafka = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='copyPendingToKafka', args=sgqlc.types.ArgDict((
        ('topic', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='topic', default=None)),
))
    )
    reprocess_message = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='reprocessMessage', args=sgqlc.types.ArgDict((
        ('message_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='messageId', default=None)),
        ('topic', sgqlc.types.Arg(ID, graphql_name='topic', default=None)),
))
    )
    reprocess_messages = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='reprocessMessages', args=sgqlc.types.ArgDict((
        ('message_ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='messageIds', default=None)),
        ('topic', sgqlc.types.Arg(ID, graphql_name='topic', default=None)),
))
    )
    update_exporter = sgqlc.types.Field(sgqlc.types.non_null('Exporter'), graphql_name='updateExporter', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('data', sgqlc.types.Arg(sgqlc.types.non_null(ExporterInput), graphql_name='data', default=None)),
))
    )
    add_exporter_task = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='addExporterTask', args=sgqlc.types.ArgDict((
        ('exporter', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='exporter', default=None)),
        ('task', sgqlc.types.Arg(sgqlc.types.non_null(ExportTaskInput), graphql_name='task', default=None)),
))
    )
    cancel_export_task = sgqlc.types.Field(sgqlc.types.non_null('ExportTask'), graphql_name='cancelExportTask', args=sgqlc.types.ArgDict((
        ('task_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='taskId', default=None)),
))
    )
    add_concept_transform_config = sgqlc.types.Field(sgqlc.types.non_null('ConceptTransformConfig'), graphql_name='addConceptTransformConfig', args=sgqlc.types.ArgDict((
        ('concept_transform', sgqlc.types.Arg(sgqlc.types.non_null(ConceptTransformConfigInput), graphql_name='conceptTransform', default=None)),
))
    )
    copy_concept_transform_config = sgqlc.types.Field(sgqlc.types.non_null('ConceptTransformConfig'), graphql_name='copyConceptTransformConfig', args=sgqlc.types.ArgDict((
        ('source_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='sourceId', default=None)),
        ('title', sgqlc.types.Arg(String, graphql_name='title', default=None)),
))
    )
    update_concept_transform_config = sgqlc.types.Field(sgqlc.types.non_null('ConceptTransformConfig'), graphql_name='updateConceptTransformConfig', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('concept_transform', sgqlc.types.Arg(sgqlc.types.non_null(ConceptTransformConfigInput), graphql_name='conceptTransform', default=None)),
))
    )
    update_concept_transform_config_transforms = sgqlc.types.Field(sgqlc.types.non_null('ConceptTransformConfig'), graphql_name='updateConceptTransformConfigTransforms', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('transforms', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(PipelineTransformSetupInput))), graphql_name='transforms', default=None)),
))
    )
    delete_concept_transform_config = sgqlc.types.Field(sgqlc.types.non_null('ConceptTransformConfig'), graphql_name='deleteConceptTransformConfig', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    add_concept_transform_task = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='addConceptTransformTask', args=sgqlc.types.ArgDict((
        ('task', sgqlc.types.Arg(sgqlc.types.non_null(ConceptTransformTaskInput), graphql_name='task', default=None)),
))
    )
    cancel_concept_transform_task = sgqlc.types.Field(sgqlc.types.non_null('ConceptTransformTask'), graphql_name='cancelConceptTransformTask', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    add_user_pipeline_transform = sgqlc.types.Field(sgqlc.types.non_null('UserPipelineTransform'), graphql_name='addUserPipelineTransform', args=sgqlc.types.ArgDict((
        ('description', sgqlc.types.Arg(String, graphql_name='description', default=None)),
        ('service_image', sgqlc.types.Arg(Upload, graphql_name='serviceImage', default=None)),
        ('service', sgqlc.types.Arg(UserServiceInput, graphql_name='service', default=None)),
))
    )
    update_user_pipeline_transform = sgqlc.types.Field(sgqlc.types.non_null('UserPipelineTransform'), graphql_name='updateUserPipelineTransform', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('description', sgqlc.types.Arg(String, graphql_name='description', default=None)),
        ('service_image', sgqlc.types.Arg(Upload, graphql_name='serviceImage', default=None)),
        ('service', sgqlc.types.Arg(UserServiceInput, graphql_name='service', default=None)),
))
    )
    delete_user_pipeline_transform = sgqlc.types.Field(sgqlc.types.non_null('UserPipelineTransform'), graphql_name='deleteUserPipelineTransform', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    service_stats = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ServiceStats'))), graphql_name='serviceStats', args=sgqlc.types.ArgDict((
        ('reset', sgqlc.types.Arg(Boolean, graphql_name='reset', default=False)),
))
    )
    add_user = sgqlc.types.Field('User', graphql_name='addUser', args=sgqlc.types.ArgDict((
        ('create_user_params', sgqlc.types.Arg(sgqlc.types.non_null(CreateUserParams), graphql_name='createUserParams', default=None)),
))
    )
    update_user_password = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateUserPassword', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('password', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='password', default=None)),
))
    )
    update_current_user_password = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateCurrentUserPassword', args=sgqlc.types.ArgDict((
        ('old_password', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='oldPassword', default=None)),
        ('password', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='password', default=None)),
))
    )
    update_current_user = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateCurrentUser', args=sgqlc.types.ArgDict((
        ('update_current_user_params', sgqlc.types.Arg(sgqlc.types.non_null(UpdateCurrentUserParams), graphql_name='updateCurrentUserParams', default=None)),
))
    )
    update_user = sgqlc.types.Field('User', graphql_name='updateUser', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('update_user_params', sgqlc.types.Arg(sgqlc.types.non_null(UpdateUserParams), graphql_name='updateUserParams', default=None)),
))
    )
    update_user_attributes = sgqlc.types.Field(sgqlc.types.non_null('UserWithError'), graphql_name='updateUserAttributes', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('attributes', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(UserAttributeInput))), graphql_name='attributes', default=None)),
))
    )
    delete_user = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteUser', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    set_kvstore_item = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='setKVStoreItem', args=sgqlc.types.ArgDict((
        ('key', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='key', default=None)),
        ('value', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='value', default=None)),
))
    )
    delete_kvstore_item = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteKVStoreItem', args=sgqlc.types.ArgDict((
        ('key', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='key', default=None)),
))
    )
    add_user_group = sgqlc.types.Field('UserGroup', graphql_name='addUserGroup', args=sgqlc.types.ArgDict((
        ('create_user_group_params', sgqlc.types.Arg(sgqlc.types.non_null(CreateUserGroupParams), graphql_name='createUserGroupParams', default=None)),
))
    )
    update_user_group = sgqlc.types.Field(sgqlc.types.non_null('UserGroup'), graphql_name='updateUserGroup', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('update_user_group_params', sgqlc.types.Arg(sgqlc.types.non_null(UpdateUserGroupParams), graphql_name='updateUserGroupParams', default=None)),
))
    )
    update_user_group_attributes = sgqlc.types.Field(sgqlc.types.non_null('UserGroupWithError'), graphql_name='updateUserGroupAttributes', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('attributes', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(UserAttributeInput))), graphql_name='attributes', default=None)),
))
    )
    delete_user_group = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteUserGroup', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    add_user_group_members = sgqlc.types.Field(sgqlc.types.non_null('StateWithError'), graphql_name='addUserGroupMembers', args=sgqlc.types.ArgDict((
        ('add_user_group_members_params', sgqlc.types.Arg(sgqlc.types.non_null(AddUserGroupMembersParams), graphql_name='addUserGroupMembersParams', default=None)),
))
    )
    delete_user_group_members = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteUserGroupMembers', args=sgqlc.types.ArgDict((
        ('delete_user_group_member_params', sgqlc.types.Arg(sgqlc.types.non_null(DeleteUserGroupMemberParams), graphql_name='deleteUserGroupMemberParams', default=None)),
))
    )
    update_event_is_read = sgqlc.types.Field(sgqlc.types.non_null(Event), graphql_name='updateEventIsRead', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('is_read', sgqlc.types.Arg(sgqlc.types.non_null(Boolean), graphql_name='isRead', default=None)),
))
    )
    read_events = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='readEvents')
    grant_access = sgqlc.types.Field('MutationResult', graphql_name='grantAccess', args=sgqlc.types.ArgDict((
        ('search_object_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='searchObjectId', default=None)),
        ('target_user_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='targetUserId', default=None)),
))
    )
    revoke_access = sgqlc.types.Field('MutationResult', graphql_name='revokeAccess', args=sgqlc.types.ArgDict((
        ('search_object_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='searchObjectId', default=None)),
        ('target_user_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='targetUserId', default=None)),
))
    )
    add_external_search_job = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('ExternalSearch')), graphql_name='addExternalSearchJob', args=sgqlc.types.ArgDict((
        ('search_objects_ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='searchObjectsIds', default=None)),
        ('concept_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='conceptId', default=None)),
))
    )
    delete_external_search_job_by_search_job_ids = sgqlc.types.Field('MutationResult', graphql_name='deleteExternalSearchJobBySearchJobIds', args=sgqlc.types.ArgDict((
        ('search_job_ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='searchJobIds', default=None)),
))
    )
    add_search_query = sgqlc.types.Field('SearchObject', graphql_name='addSearchQuery', args=sgqlc.types.ArgDict((
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
        ('search_container', sgqlc.types.Arg(sgqlc.types.non_null(SearchQueryInput), graphql_name='searchContainer', default=None)),
        ('target', sgqlc.types.Arg(sgqlc.types.non_null(SearchTarget), graphql_name='target', default=None)),
))
    )
    add_filter_settings = sgqlc.types.Field('SearchObject', graphql_name='addFilterSettings', args=sgqlc.types.ArgDict((
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
        ('search_container', sgqlc.types.Arg(sgqlc.types.non_null(FilterSettingsInput), graphql_name='searchContainer', default=None)),
        ('target', sgqlc.types.Arg(sgqlc.types.non_null(SearchTarget), graphql_name='target', default=None)),
))
    )
    add_search_query_of_concept = sgqlc.types.Field('SearchObject', graphql_name='addSearchQueryOfConcept', args=sgqlc.types.ArgDict((
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
        ('search_container', sgqlc.types.Arg(sgqlc.types.non_null(SearchQueryInput), graphql_name='searchContainer', default=None)),
))
    )
    add_filter_settings_of_concept = sgqlc.types.Field('SearchObject', graphql_name='addFilterSettingsOfConcept', args=sgqlc.types.ArgDict((
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
        ('search_container', sgqlc.types.Arg(sgqlc.types.non_null(FilterSettingsInput), graphql_name='searchContainer', default=None)),
))
    )
    add_external_search_object = sgqlc.types.Field('SearchObject', graphql_name='addExternalSearchObject', args=sgqlc.types.ArgDict((
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
        ('search_container', sgqlc.types.Arg(sgqlc.types.non_null(ExternalSearchJobConfigInput), graphql_name='searchContainer', default=None)),
))
    )
    add_external_dbobject = sgqlc.types.Field('SearchObject', graphql_name='addExternalDBObject', args=sgqlc.types.ArgDict((
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
        ('access_level', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='accessLevel', default=None)),
        ('trust_level', sgqlc.types.Arg(sgqlc.types.non_null(TrustLevel), graphql_name='trustLevel', default=None)),
        ('topic', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='topic', default=None)),
        ('task_config', sgqlc.types.Arg(sgqlc.types.non_null(DBConfigInput), graphql_name='taskConfig', default=None)),
        ('concept_type_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='conceptTypeId', default=None)),
        ('noisy_jobs_count', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='noisyJobsCount', default=None)),
))
    )
    add_external_file_repository_object = sgqlc.types.Field('SearchObject', graphql_name='addExternalFileRepositoryObject', args=sgqlc.types.ArgDict((
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
        ('access_level', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='accessLevel', default=None)),
        ('trust_level', sgqlc.types.Arg(sgqlc.types.non_null(TrustLevel), graphql_name='trustLevel', default=None)),
        ('topic', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='topic', default=None)),
        ('task_config', sgqlc.types.Arg(sgqlc.types.non_null(FileRepositoryConfigInput), graphql_name='taskConfig', default=None)),
        ('concept_type_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='conceptTypeId', default=None)),
        ('noisy_jobs_count', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='noisyJobsCount', default=None)),
))
    )
    update_search_query = sgqlc.types.Field('SearchObject', graphql_name='updateSearchQuery', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
        ('search_container', sgqlc.types.Arg(sgqlc.types.non_null(SearchQueryInput), graphql_name='searchContainer', default=None)),
))
    )
    update_filter_settings = sgqlc.types.Field('SearchObject', graphql_name='updateFilterSettings', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
        ('search_container', sgqlc.types.Arg(sgqlc.types.non_null(FilterSettingsInput), graphql_name='searchContainer', default=None)),
))
    )
    update_search_query_of_concept = sgqlc.types.Field('SearchObject', graphql_name='updateSearchQueryOfConcept', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
        ('search_container', sgqlc.types.Arg(sgqlc.types.non_null(SearchQueryInput), graphql_name='searchContainer', default=None)),
))
    )
    update_external_search_object = sgqlc.types.Field('SearchObject', graphql_name='updateExternalSearchObject', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
        ('search_container', sgqlc.types.Arg(sgqlc.types.non_null(ExternalSearchJobConfigInput), graphql_name='searchContainer', default=None)),
))
    )
    update_external_dbobject = sgqlc.types.Field('SearchObject', graphql_name='updateExternalDBObject', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
        ('concept_type_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='conceptTypeId', default=None)),
        ('access_level', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='accessLevel', default=None)),
        ('trust_level', sgqlc.types.Arg(sgqlc.types.non_null(TrustLevel), graphql_name='trustLevel', default=None)),
        ('topic', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='topic', default=None)),
        ('task_config', sgqlc.types.Arg(sgqlc.types.non_null(DBConfigInput), graphql_name='taskConfig', default=None)),
        ('noisy_jobs_count', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='noisyJobsCount', default=None)),
))
    )
    update_external_file_repository_object = sgqlc.types.Field('SearchObject', graphql_name='updateExternalFileRepositoryObject', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
        ('concept_type_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='conceptTypeId', default=None)),
        ('access_level', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='accessLevel', default=None)),
        ('trust_level', sgqlc.types.Arg(sgqlc.types.non_null(TrustLevel), graphql_name='trustLevel', default=None)),
        ('topic', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='topic', default=None)),
        ('task_config', sgqlc.types.Arg(sgqlc.types.non_null(FileRepositoryConfigInput), graphql_name='taskConfig', default=None)),
        ('noisy_jobs_count', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='noisyJobsCount', default=None)),
))
    )
    update_filter_settings_of_concept = sgqlc.types.Field('SearchObject', graphql_name='updateFilterSettingsOfConcept', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
        ('search_container', sgqlc.types.Arg(sgqlc.types.non_null(FilterSettingsInput), graphql_name='searchContainer', default=None)),
))
    )
    delete_search_objects = sgqlc.types.Field('MutationResult', graphql_name='deleteSearchObjects', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids', default=None)),
))
    )
    add_noisy_file = sgqlc.types.Field(ID, graphql_name='addNoisyFile', args=sgqlc.types.ArgDict((
        ('file', sgqlc.types.Arg(sgqlc.types.non_null(Upload), graphql_name='file', default=None)),
        ('property_type_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='propertyTypeId', default=None)),
))
    )
    delete_noisy_file = sgqlc.types.Field('MutationResult', graphql_name='deleteNoisyFile', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids', default=None)),
))
    )


class MutationResult(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('result',)
    result = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='result')


class NERCRegexp(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('regexp', 'context_regexp', 'auto_create')
    regexp = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='regexp')
    context_regexp = sgqlc.types.Field(String, graphql_name='contextRegexp')
    auto_create = sgqlc.types.Field(Boolean, graphql_name='autoCreate')


class NamedValue(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('id', 'property_value_type', 'value')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    property_value_type = sgqlc.types.Field(sgqlc.types.non_null(CompositePropertyValueType), graphql_name='propertyValueType')
    value = sgqlc.types.Field(sgqlc.types.non_null('Value'), graphql_name='value')


class NoisyFile(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('id', 'file_name', 'concept_property_type', 'noisy_values_count', 'creator_id', 'updater_id', 'created_at', 'updated_at')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    file_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='fileName')
    concept_property_type = sgqlc.types.Field(sgqlc.types.non_null('ConceptPropertyType'), graphql_name='conceptPropertyType')
    noisy_values_count = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='noisyValuesCount')
    creator_id = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='creatorId')
    updater_id = sgqlc.types.Field('User', graphql_name='updaterId')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(UnixTime), graphql_name='createdAt')
    updated_at = sgqlc.types.Field(UnixTime, graphql_name='updatedAt')


class NoisyFileContent(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('file_name', 'file_content', 'concept_property_type', 'noisy_values_count')
    file_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='fileName')
    file_content = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='fileContent')
    concept_property_type = sgqlc.types.Field(sgqlc.types.non_null('ConceptPropertyType'), graphql_name='conceptPropertyType')
    noisy_values_count = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='noisyValuesCount')


class Organization(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('concept', 'industry', 'attack_amount', 'delta', 'history', 'severity_class')
    concept = sgqlc.types.Field(sgqlc.types.non_null('Concept'), graphql_name='concept')
    industry = sgqlc.types.Field(String, graphql_name='industry')
    attack_amount = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='attackAmount')
    delta = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='delta')
    history = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(CountDateValue)), graphql_name='history')
    severity_class = sgqlc.types.Field(sgqlc.types.non_null(SeverityCategories), graphql_name='severityClass')


class OrganizationObject(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('organization', 'max_history_value', 'history_count', 'next_date')
    organization = sgqlc.types.Field(sgqlc.types.non_null(Organization), graphql_name='organization')
    max_history_value = sgqlc.types.Field(Int, graphql_name='maxHistoryValue')
    history_count = sgqlc.types.Field(Int, graphql_name='historyCount')
    next_date = sgqlc.types.Field(String, graphql_name='nextDate')


class OutputLimiter(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('maximum_points', 'minimum_number')
    maximum_points = sgqlc.types.Field(Long, graphql_name='maximumPoints')
    minimum_number = sgqlc.types.Field(Long, graphql_name='minimumNumber')


class PaginationAPTGroups(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('total', 'list_apt_groups', 'max_history_value', 'history_count', 'next_date')
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')
    list_apt_groups = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(APTGroup))), graphql_name='listAptGroups')
    max_history_value = sgqlc.types.Field(Int, graphql_name='maxHistoryValue')
    history_count = sgqlc.types.Field(Int, graphql_name='historyCount')
    next_date = sgqlc.types.Field(String, graphql_name='nextDate')


class PaginationExploits(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('total', 'list_expl', 'max_history_value', 'history_count', 'next_date')
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')
    list_expl = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Exploit))), graphql_name='listExpl')
    max_history_value = sgqlc.types.Field(Int, graphql_name='maxHistoryValue')
    history_count = sgqlc.types.Field(Int, graphql_name='historyCount')
    next_date = sgqlc.types.Field(String, graphql_name='nextDate')


class PaginationExternalSearch(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('total', 'list_external_search')
    total = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='total')
    list_external_search = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ExternalSearch'))), graphql_name='listExternalSearch')


class PaginationInformationSource(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('total', 'list_information_source')
    total = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='total')
    list_information_source = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(InformationSource))), graphql_name='listInformationSource')


class PaginationInformationSourceLoader(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('list_information_source_loader', 'total')
    list_information_source_loader = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('InformationSourceLoader'))), graphql_name='listInformationSourceLoader')
    total = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='total')


class PaginationJob(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('list_job', 'total')
    list_job = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Job'))), graphql_name='listJob')
    total = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='total')


class PaginationLog(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('total', 'log_list')
    total = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='total')
    log_list = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Log))), graphql_name='logList')


class PaginationMalwares(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('total', 'list_mal', 'max_history_value', 'history_count', 'next_date')
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')
    list_mal = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Malware))), graphql_name='listMal')
    max_history_value = sgqlc.types.Field(Int, graphql_name='maxHistoryValue')
    history_count = sgqlc.types.Field(Int, graphql_name='historyCount')
    next_date = sgqlc.types.Field(String, graphql_name='nextDate')


class PaginationMetric(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('total', 'metric_list')
    total = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='total')
    metric_list = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Metric))), graphql_name='metricList')


class PaginationOrganizations(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('total', 'list_org', 'max_history_value', 'history_count', 'next_date')
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')
    list_org = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Organization))), graphql_name='listOrg')
    max_history_value = sgqlc.types.Field(Int, graphql_name='maxHistoryValue')
    history_count = sgqlc.types.Field(Int, graphql_name='historyCount')
    next_date = sgqlc.types.Field(String, graphql_name='nextDate')


class PaginationPeriodicTask(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('total', 'list_periodic_task')
    total = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='total')
    list_periodic_task = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('PeriodicTask'))), graphql_name='listPeriodicTask')


class PaginationRequest(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('total', 'request_list')
    total = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='total')
    request_list = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Request'))), graphql_name='requestList')


class PaginationSearchObject(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('list_search_object', 'total')
    list_search_object = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('SearchObject'))), graphql_name='listSearchObject')
    total = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='total')


class PaginationSoftwareVulns(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('total', 'list_software_vuln', 'max_history_value', 'history_count', 'next_date')
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')
    list_software_vuln = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('SoftwareVuln'))), graphql_name='listSoftwareVuln')
    max_history_value = sgqlc.types.Field(Int, graphql_name='maxHistoryValue')
    history_count = sgqlc.types.Field(Int, graphql_name='historyCount')
    next_date = sgqlc.types.Field(String, graphql_name='nextDate')


class PaginationVulns(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('total', 'list_vuln', 'max_history_value', 'history_count', 'next_date')
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')
    list_vuln = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Vulnerability'))), graphql_name='listVuln')
    max_history_value = sgqlc.types.Field(Int, graphql_name='maxHistoryValue')
    history_count = sgqlc.types.Field(Int, graphql_name='historyCount')
    next_date = sgqlc.types.Field(String, graphql_name='nextDate')


class ParagraphMetadata(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('page_id', 'line_id', 'original_text', 'hidden', 'text_translations', 'paragraph_type')
    page_id = sgqlc.types.Field(Int, graphql_name='pageId')
    line_id = sgqlc.types.Field(Int, graphql_name='lineId')
    original_text = sgqlc.types.Field(String, graphql_name='originalText')
    hidden = sgqlc.types.Field(Boolean, graphql_name='hidden')
    text_translations = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('Translation')), graphql_name='textTranslations')
    paragraph_type = sgqlc.types.Field(sgqlc.types.non_null(NodeType), graphql_name='paragraphType')


class Parameter(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('key', 'value')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')
    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='value')


class ParamsSchema(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('schema', 'ui_schema')
    schema = sgqlc.types.Field(sgqlc.types.non_null(JSON), graphql_name='schema')
    ui_schema = sgqlc.types.Field(JSON, graphql_name='uiSchema')


class PdfSpecificMetadataGQL(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('author', 'creation_date')
    author = sgqlc.types.Field(String, graphql_name='author')
    creation_date = sgqlc.types.Field(UnixTime, graphql_name='creationDate')


class PendingMessageList(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('messages', 'total')
    messages = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('PendingMessageStatus'))), graphql_name='messages')
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')


class PendingMessageStatus(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('id', 'info')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    info = sgqlc.types.Field(sgqlc.types.non_null('PendingMessageStatusInfo'), graphql_name='info')


class PeriodicJobData(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('id', 'name')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')


class PeriodicJobMetrics(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('periodic_job_id', 'metrics')
    periodic_job_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='periodicJobId')
    metrics = sgqlc.types.Field(sgqlc.types.non_null(MessageMetrics), graphql_name='metrics')


class PeriodicJobPagination(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('total', 'list_periodic_job')
    total = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='total')
    list_periodic_job = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('PeriodicJob'))), graphql_name='listPeriodicJob')


class PeriodicTaskImportMetrics(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('errors_count',)
    errors_count = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='errorsCount')


class PeriodicTaskMetrics(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('periodic_task_id', 'metrics')
    periodic_task_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='periodicTaskId')
    metrics = sgqlc.types.Field(sgqlc.types.non_null(MessageMetrics), graphql_name='metrics')


class PipelineConfigList(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('pipeline_configs', 'total')
    pipeline_configs = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('PipelineConfig'))), graphql_name='pipelineConfigs')
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')


class PipelineSetup(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('pipeline_config',)
    pipeline_config = sgqlc.types.Field(sgqlc.types.non_null('PipelineConfig'), graphql_name='pipelineConfig')


class PipelineTransform(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('id', 'description', 'in_type', 'out_type', 'params_schema', 'version')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='description')
    in_type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='inType')
    out_type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='outType')
    params_schema = sgqlc.types.Field(sgqlc.types.non_null(ParamsSchema), graphql_name='paramsSchema')
    version = sgqlc.types.Field(String, graphql_name='version')


class PipelineTransformList(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('transforms', 'total')
    transforms = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(PipelineTransform))), graphql_name='transforms')
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')


class PipelineTransformSetup(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('id', 'params', 'transform')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    params = sgqlc.types.Field(sgqlc.types.non_null(JSON), graphql_name='params')
    transform = sgqlc.types.Field(sgqlc.types.non_null(PipelineTransform), graphql_name='transform')


class PlatformFacet(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('value', 'count')
    value = sgqlc.types.Field(sgqlc.types.non_null('Platform'), graphql_name='value')
    count = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='count')


class PlatformPagination(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('list_platform', 'total')
    list_platform = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Platform'))), graphql_name='listPlatform')
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')


class PlatformStatistics(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('count_account', 'count_doc', 'count_doc_today', 'count_doc_week', 'count_doc_month', 'recall_doc_today', 'recall_doc_week', 'recall_doc_month')
    count_account = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='countAccount')
    count_doc = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='countDoc')
    count_doc_today = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='countDocToday')
    count_doc_week = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='countDocWeek')
    count_doc_month = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='countDocMonth')
    recall_doc_today = sgqlc.types.Field(sgqlc.types.non_null(DocumentRecall), graphql_name='recallDocToday')
    recall_doc_week = sgqlc.types.Field(sgqlc.types.non_null(DocumentRecall), graphql_name='recallDocWeek')
    recall_doc_month = sgqlc.types.Field(sgqlc.types.non_null(DocumentRecall), graphql_name='recallDocMonth')


class ProjectData(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('id', 'title')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')


class ProjectHistogram(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('project_name', 'items_scraped_count', 'jobs_count', 'jobs_with_errors_logs')
    project_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='projectName')
    items_scraped_count = sgqlc.types.Field(Long, graphql_name='itemsScrapedCount')
    jobs_count = sgqlc.types.Field(Int, graphql_name='jobsCount')
    jobs_with_errors_logs = sgqlc.types.Field(Int, graphql_name='jobsWithErrorsLogs')


class ProjectPagination(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('total', 'list_project')
    total = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='total')
    list_project = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Project'))), graphql_name='listProject')


class ProjectStats(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('items_scraped_count', 'errors_count', 'jobs_count', 'jobs_with_errors_logs_count', 'job_ids_with_error_logs', 'jobs_with_critical_logs_count')
    items_scraped_count = sgqlc.types.Field(Long, graphql_name='itemsScrapedCount')
    errors_count = sgqlc.types.Field(Int, graphql_name='errorsCount')
    jobs_count = sgqlc.types.Field(Int, graphql_name='jobsCount')
    jobs_with_errors_logs_count = sgqlc.types.Field(Int, graphql_name='jobsWithErrorsLogsCount')
    job_ids_with_error_logs = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Long))), graphql_name='jobIdsWithErrorLogs')
    jobs_with_critical_logs_count = sgqlc.types.Field(Int, graphql_name='jobsWithCriticalLogsCount')


class Query(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('software', 'vulnerability', 'exploit', 'malware', 'apt_group', 'organization', 'pagination_software_vulns', 'pagination_cwe', 'pagination_software_names', 'pagination_exploit_names', 'pagination_vulnerability_names', 'pagination_vulns', 'pagination_exploits', 'pagination_malwares', 'pagination_aptgroups', 'pagination_organizations', 'industries', 'soft_types', 'dashboard_layout', 'dashboard_panel', 'get_dashboards', 'get_dashboard', 'get_chart_grouping_step_options', 'get_entity_field_options', 'preview_chart_panel', 'image_with_thumbnail', 'images_with_thumbnail', 'generate_external_url', 'task', 'pagination_task', 'check_connection', 'pagination_task_logs', 'execute_query_to_outer_db', 'periodic_task', 'pagination_periodic_task', 'pagination_periodic_task_logs', 'analytics', 'crawler', 'list_crawler', 'pagination_crawler', 'crawler_args_and_settings_description', 'credential', 'pagination_credential', 'job', 'list_job', 'pagination_job_logs', 'pagination_job_requests', 'pagination_job_metrics', 'pagination_job', 'periodic_job', 'pagination_periodic_job', 'pagination_periodic_job_logs', 'pagination_periodic_job_requests', 'pagination_periodic_job_metrics', 'check_periodic_job_by_input', 'project', 'pagination_project', 'project_args_and_settings_description', 'project_default_args_and_settings_description', 'information_source_loader', 'pagination_information_source_loader', 'information_source', 'pagination_information_source', 'version', 'list_version', 'pagination_versions_crawler', 'pagination_egg_file_versions_project', 'web_scraper_version_is_compatible', 'document', 'story', 'pagination_story', 'pagination_document_markers', 'concept_type', 'composite_concept_type', 'pagination_composite_concept_type', 'concept_property_type', 'concept_link_type', 'concept_property_value_type', 'list_concept_type', 'list_user_menu_type', 'list_concept_property_type', 'list_concept_property_type_by_id', 'list_concept_link_type', 'list_concept_property_value_type', 'pagination_concept_type', 'pagination_concept_property_type', 'pagination_concept_link_property_type', 'pagination_concept_link_type', 'pagination_concept_property_value_type', 'composite_concept_property_type', 'composite_link_property_type', 'list_composite_concept_property_type', 'list_composite_link_property_type', 'pagination_composite_concept_property_type', 'pagination_composite_link_property_type', 'composite_property_value_template', 'list_composite_property_value_template', 'pagination_composite_property_value_template', 'concept_type_view', 'domain_map', 'concept', 'list_concept_by_id', 'pagination_concept', 'composite_concept', 'pagination_composite_concept', 'list_concept_link_between_fixed_concepts', 'concept_property', 'concept_link', 'pagination_concept_link', 'pagination_kbrelated_document', 'issue', 'pagination_issue', 'pagination_issue_change', 'research_map', 'pagination_research_map', 'active_research_map', 'list_top_neighbors_on_map', 'list_last_research_map', 'document_autocomplete', 'concept_autocomplete', 'get_osm_place_name', 'get_osm_coordinates', 'access_level', 'pagination_access_level', 'story_fs2_query', 'concept_fs2_query', 'markers_bulk', 'platform', 'list_platform_by_id', 'pagination_platform', 'account', 'list_account_by_id', 'pagination_account', 'pagination_country', 'pagination_language', 'document_feed', 'pagination_document_feed', 'concept_registry_view', 'document_registry_view', 'document_card_view', 'chart', 'preview_chart', 'pipeline_transforms', 'pipeline_transform', 'pipeline_configs', 'pipeline_config', 'export_pipeline_config', 'kafka_pipeline_start_type', 'kafka_topics', 'kafka_topic', 'message_status', 'message_topic', 'message_statuses', 'failed_messages', 'pending_messages', 'active_messages', 'completed_ok_messages', 'duplicate_messages', 'messages_by_parent_id', 'exporter', 'exporters', 'export_task', 'export_tasks', 'job_items2', 'periodic_job_items2', 'task_items2', 'periodic_task_items2', 'job_ids_by_message_uuid2', 'job_metrics2', 'periodic_job_metrics2', 'task_metrics2', 'periodic_task_metrics2', 'concept_transform_configs', 'concept_transform_config', 'concept_transform_message_type', 'concept_transform_task', 'concept_transform_tasks', 'user_pipeline_transforms', 'user_pipeline_transform', 'user', 'current_user', 'pagination_user', 'get_kvstore_item', 'pagination_attribute', 'user_group', 'pagination_user_group', 'event', 'pagination_event', 'list_external_search_jobs_by_job_ids', 'list_external_search_tasks_by_task_ids', 'pagination_external_search', 'pagination_noisy_jobs_by_primary_job', 'list_search_objects_of_concept', 'search_object', 'search_object_with_nested', 'list_search_objects', 'pagination_search_objects', 'name_autocomplete', 'noisy_file', 'noisy_file_by_concept_property_type_id', 'noisy_file_content', 'language', 'language_list_by_id', 'detect_language', 'translate_str', 'source_languages', 'default_language')
    software = sgqlc.types.Field('SoftwareVulnObject', graphql_name='software', args=sgqlc.types.ArgDict((
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(RiverEntityFilterSettings), graphql_name='filterSettings', default=None)),
        ('soft_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='softId', default=None)),
))
    )
    vulnerability = sgqlc.types.Field('VulnerabilityObject', graphql_name='vulnerability', args=sgqlc.types.ArgDict((
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(RiverEntityFilterSettings), graphql_name='filterSettings', default=None)),
        ('cve_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='cveId', default=None)),
))
    )
    exploit = sgqlc.types.Field(ExploitObject, graphql_name='exploit', args=sgqlc.types.ArgDict((
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(RiverEntityFilterSettings), graphql_name='filterSettings', default=None)),
        ('exploit_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='exploitId', default=None)),
))
    )
    malware = sgqlc.types.Field(MalwareObject, graphql_name='malware', args=sgqlc.types.ArgDict((
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(RiverEntityFilterSettings), graphql_name='filterSettings', default=None)),
        ('malware_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='malwareId', default=None)),
))
    )
    apt_group = sgqlc.types.Field(APTGroupObject, graphql_name='aptGroup', args=sgqlc.types.ArgDict((
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(RiverEntityFilterSettings), graphql_name='filterSettings', default=None)),
        ('apt_group_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='aptGroupId', default=None)),
))
    )
    organization = sgqlc.types.Field(OrganizationObject, graphql_name='organization', args=sgqlc.types.ArgDict((
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(RiverEntityFilterSettings), graphql_name='filterSettings', default=None)),
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='organizationId', default=None)),
))
    )
    pagination_software_vulns = sgqlc.types.Field(sgqlc.types.non_null(PaginationSoftwareVulns), graphql_name='paginationSoftwareVulns', args=sgqlc.types.ArgDict((
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(PaginationSoftwareVulnsFilterSettings), graphql_name='filterSettings', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('direction', sgqlc.types.Arg(SortDirection, graphql_name='direction', default=None)),
        ('sort_field', sgqlc.types.Arg(SoftVulnSortColumns, graphql_name='sortField', default=None)),
))
    )
    pagination_cwe = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Concept'))), graphql_name='paginationCWE', args=sgqlc.types.ArgDict((
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(PaginationCWEFilterSettings), graphql_name='filterSettings', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('direction', sgqlc.types.Arg(SortDirection, graphql_name='direction', default=None)),
        ('sort_field', sgqlc.types.Arg(CWESortColumns, graphql_name='sortField', default=None)),
))
    )
    pagination_software_names = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Concept'))), graphql_name='paginationSoftwareNames', args=sgqlc.types.ArgDict((
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(PaginationSoftwareNamesFilterSettings), graphql_name='filterSettings', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('direction', sgqlc.types.Arg(SortDirection, graphql_name='direction', default=None)),
        ('sort_field', sgqlc.types.Arg(SoftwareNamesSortColumns, graphql_name='sortField', default=None)),
))
    )
    pagination_exploit_names = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Concept'))), graphql_name='paginationExploitNames', args=sgqlc.types.ArgDict((
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(PaginationExploitNamesFilterSettings), graphql_name='filterSettings', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('direction', sgqlc.types.Arg(SortDirection, graphql_name='direction', default=None)),
        ('sort_field', sgqlc.types.Arg(ExploitNamesSortColumns, graphql_name='sortField', default=None)),
))
    )
    pagination_vulnerability_names = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Concept'))), graphql_name='paginationVulnerabilityNames', args=sgqlc.types.ArgDict((
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(PaginationVulnerabilityNamesFilterSettings), graphql_name='filterSettings', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('direction', sgqlc.types.Arg(SortDirection, graphql_name='direction', default=None)),
        ('sort_field', sgqlc.types.Arg(VulnerabilityNamesSortColumns, graphql_name='sortField', default=None)),
))
    )
    pagination_vulns = sgqlc.types.Field(sgqlc.types.non_null(PaginationVulns), graphql_name='paginationVulns', args=sgqlc.types.ArgDict((
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(PaginationVulnsFilterSettings), graphql_name='filterSettings', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('direction', sgqlc.types.Arg(SortDirection, graphql_name='direction', default=None)),
        ('sort_field', sgqlc.types.Arg(VulnSortColumns, graphql_name='sortField', default=None)),
))
    )
    pagination_exploits = sgqlc.types.Field(sgqlc.types.non_null(PaginationExploits), graphql_name='paginationExploits', args=sgqlc.types.ArgDict((
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(PaginationExploitsFilterSettings), graphql_name='filterSettings', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('direction', sgqlc.types.Arg(SortDirection, graphql_name='direction', default=None)),
        ('sort_field', sgqlc.types.Arg(ExplSortColumns, graphql_name='sortField', default=None)),
))
    )
    pagination_malwares = sgqlc.types.Field(sgqlc.types.non_null(PaginationMalwares), graphql_name='paginationMalwares', args=sgqlc.types.ArgDict((
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(PaginationMalwaresFilterSettings), graphql_name='filterSettings', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('direction', sgqlc.types.Arg(SortDirection, graphql_name='direction', default=None)),
        ('sort_field', sgqlc.types.Arg(MalwSortColumns, graphql_name='sortField', default=None)),
))
    )
    pagination_aptgroups = sgqlc.types.Field(sgqlc.types.non_null(PaginationAPTGroups), graphql_name='paginationAPTGroups', args=sgqlc.types.ArgDict((
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(PaginationAPTGroupsFilterSettings), graphql_name='filterSettings', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('direction', sgqlc.types.Arg(SortDirection, graphql_name='direction', default=None)),
        ('sort_field', sgqlc.types.Arg(APTSortColumns, graphql_name='sortField', default=None)),
))
    )
    pagination_organizations = sgqlc.types.Field(sgqlc.types.non_null(PaginationOrganizations), graphql_name='paginationOrganizations', args=sgqlc.types.ArgDict((
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(PaginationOrganizationsFilterSettings), graphql_name='filterSettings', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('direction', sgqlc.types.Arg(SortDirection, graphql_name='direction', default=None)),
        ('sort_field', sgqlc.types.Arg(OrgSortColumns, graphql_name='sortField', default=None)),
))
    )
    industries = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='industries', args=sgqlc.types.ArgDict((
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(IndustryFilterSettings), graphql_name='filterSettings', default=None)),
))
    )
    soft_types = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='softTypes', args=sgqlc.types.ArgDict((
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(SoftTypeFilterSettings), graphql_name='filterSettings', default=None)),
))
    )
    dashboard_layout = sgqlc.types.Field(sgqlc.types.non_null(DashboardLayout), graphql_name='dashboardLayout', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(ID, graphql_name='id', default='')),
))
    )
    dashboard_panel = sgqlc.types.Field(sgqlc.types.non_null(DashboardPanel), graphql_name='dashboardPanel', args=sgqlc.types.ArgDict((
        ('i', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='i', default=None)),
        ('id', sgqlc.types.Arg(ID, graphql_name='id', default='')),
))
    )
    get_dashboards = sgqlc.types.Field(sgqlc.types.non_null(Dashboards), graphql_name='getDashboards')
    get_dashboard = sgqlc.types.Field(sgqlc.types.non_null(Dashboard), graphql_name='getDashboard', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(ID, graphql_name='id', default='')),
))
    )
    get_chart_grouping_step_options = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(GroupingStepOption)), graphql_name='getChartGroupingStepOptions', args=sgqlc.types.ArgDict((
        ('target', sgqlc.types.Arg(sgqlc.types.non_null(ChartRTarget), graphql_name='target', default=None)),
        ('grouping_field', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='groupingField', default=None)),
))
    )
    get_entity_field_options = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(EntityFieldOption))), graphql_name='getEntityFieldOptions', args=sgqlc.types.ArgDict((
        ('target', sgqlc.types.Arg(sgqlc.types.non_null(ChartRTarget), graphql_name='target', default=None)),
))
    )
    preview_chart_panel = sgqlc.types.Field('ChartRData', graphql_name='previewChartPanel', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(ChartPanelInput), graphql_name='form', default=None)),
))
    )
    image_with_thumbnail = sgqlc.types.Field(Image, graphql_name='imageWithThumbnail', args=sgqlc.types.ArgDict((
        ('url', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='url', default=None)),
))
    )
    images_with_thumbnail = sgqlc.types.Field(sgqlc.types.list_of(Image), graphql_name='imagesWithThumbnail', args=sgqlc.types.ArgDict((
        ('urls', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='urls', default=None)),
))
    )
    generate_external_url = sgqlc.types.Field(String, graphql_name='generateExternalUrl', args=sgqlc.types.ArgDict((
        ('file', sgqlc.types.Arg(sgqlc.types.non_null(MinioFile), graphql_name='file', default=None)),
        ('check_exist', sgqlc.types.Arg(Boolean, graphql_name='checkExist', default=False)),
))
    )
    task = sgqlc.types.Field('Task', graphql_name='task', args=sgqlc.types.ArgDict((
        ('task_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='taskId', default=None)),
))
    )
    pagination_task = sgqlc.types.Field('TaskList', graphql_name='paginationTask', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='offset', default=None)),
        ('tasks_sort', sgqlc.types.Arg(sgqlc.types.non_null(TasksSort), graphql_name='tasksSort', default=None)),
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(TaskFilterSettings), graphql_name='filterSettings', default=None)),
))
    )
    check_connection = sgqlc.types.Field(Boolean, graphql_name='checkConnection', args=sgqlc.types.ArgDict((
        ('url', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='url', default=None)),
        ('domain', sgqlc.types.Arg(String, graphql_name='domain', default=None)),
        ('login', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='login', default=None)),
        ('password', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='password', default=None)),
))
    )
    pagination_task_logs = sgqlc.types.Field(PaginationLog, graphql_name='paginationTaskLogs', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('limit', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='offset', default=None)),
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(LogFilterSettings), graphql_name='filterSettings', default=None)),
        ('sort_field', sgqlc.types.Arg(sgqlc.types.non_null(LogSorting), graphql_name='sortField', default='timestamp')),
        ('direction', sgqlc.types.Arg(sgqlc.types.non_null(SortDirection), graphql_name='direction', default='descending')),
))
    )
    execute_query_to_outer_db = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Json)), graphql_name='executeQueryToOuterDB', args=sgqlc.types.ArgDict((
        ('url', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='url', default=None)),
        ('login', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='login', default=None)),
        ('password', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='password', default=None)),
        ('db_query_type', sgqlc.types.Arg(sgqlc.types.non_null(QueryType), graphql_name='dbQueryType', default=None)),
        ('sql_query', sgqlc.types.Arg(String, graphql_name='sqlQuery', default=None)),
        ('target_table', sgqlc.types.Arg(String, graphql_name='targetTable', default=None)),
        ('file_columns', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(FileQueryInput))), graphql_name='fileColumns', default=None)),
))
    )
    periodic_task = sgqlc.types.Field('PeriodicTask', graphql_name='periodicTask', args=sgqlc.types.ArgDict((
        ('periodic_task_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='periodicTaskId', default=None)),
))
    )
    pagination_periodic_task = sgqlc.types.Field(PaginationPeriodicTask, graphql_name='paginationPeriodicTask', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='offset', default=None)),
        ('periodic_task_filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(PeriodicTaskFilterSettingsInput), graphql_name='periodicTaskFilterSettings', default=None)),
        ('sort_field', sgqlc.types.Arg(sgqlc.types.non_null(PeriodicTaskSorting), graphql_name='sortField', default=None)),
        ('sort_direction', sgqlc.types.Arg(sgqlc.types.non_null(SortDirection), graphql_name='sortDirection', default=None)),
))
    )
    pagination_periodic_task_logs = sgqlc.types.Field(PaginationLog, graphql_name='paginationPeriodicTaskLogs', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('limit', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='offset', default=None)),
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(LogFilterSettings), graphql_name='filterSettings', default=None)),
        ('sort_field', sgqlc.types.Arg(sgqlc.types.non_null(LogSorting), graphql_name='sortField', default='timestamp')),
        ('direction', sgqlc.types.Arg(sgqlc.types.non_null(SortDirection), graphql_name='direction', default='descending')),
))
    )
    analytics = sgqlc.types.Field(sgqlc.types.non_null('Stats'), graphql_name='analytics')
    crawler = sgqlc.types.Field(sgqlc.types.non_null('Crawler'), graphql_name='crawler', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    list_crawler = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('Crawler')), graphql_name='listCrawler', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids', default=None)),
))
    )
    pagination_crawler = sgqlc.types.Field(sgqlc.types.non_null(CrawlerPagination), graphql_name='paginationCrawler', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('filter_settings', sgqlc.types.Arg(CrawlerFilterSettings, graphql_name='filterSettings', default={})),
        ('sort_field', sgqlc.types.Arg(CrawlerSorting, graphql_name='sortField', default='id')),
        ('direction', sgqlc.types.Arg(SortDirection, graphql_name='direction', default='descending')),
))
    )
    crawler_args_and_settings_description = sgqlc.types.Field(sgqlc.types.non_null(ArgsAndSettingsDescription), graphql_name='crawlerArgsAndSettingsDescription', args=sgqlc.types.ArgDict((
        ('crawler_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='crawlerId', default=None)),
        ('version_id', sgqlc.types.Arg(ID, graphql_name='versionId', default=None)),
))
    )
    credential = sgqlc.types.Field(sgqlc.types.non_null('Credential'), graphql_name='credential', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    pagination_credential = sgqlc.types.Field(sgqlc.types.non_null(CredentialPagination), graphql_name='paginationCredential', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('sort_field', sgqlc.types.Arg(CredentialSorting, graphql_name='sortField', default='id')),
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(CredentialFilterSettings), graphql_name='filterSettings', default=None)),
        ('direction', sgqlc.types.Arg(SortDirection, graphql_name='direction', default='descending')),
))
    )
    job = sgqlc.types.Field(sgqlc.types.non_null('Job'), graphql_name='job', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    list_job = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('Job')), graphql_name='listJob', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids', default=None)),
))
    )
    pagination_job_logs = sgqlc.types.Field(sgqlc.types.non_null(PaginationLog), graphql_name='paginationJobLogs', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('filter_settings', sgqlc.types.Arg(LogFilterSettings, graphql_name='filterSettings', default={})),
        ('direction', sgqlc.types.Arg(SortDirection, graphql_name='direction', default='descending')),
        ('sort_field', sgqlc.types.Arg(LogSorting, graphql_name='sortField', default=None)),
))
    )
    pagination_job_requests = sgqlc.types.Field(sgqlc.types.non_null(PaginationRequest), graphql_name='paginationJobRequests', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('filter_settings', sgqlc.types.Arg(RequestFilterSettings, graphql_name='filterSettings', default={})),
        ('direction', sgqlc.types.Arg(SortDirection, graphql_name='direction', default='descending')),
        ('sort_field', sgqlc.types.Arg(RequestSorting, graphql_name='sortField', default=None)),
))
    )
    pagination_job_metrics = sgqlc.types.Field(sgqlc.types.non_null(PaginationMetric), graphql_name='paginationJobMetrics', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('filter_settings', sgqlc.types.Arg(MetricFilterSettings, graphql_name='filterSettings', default={})),
        ('direction', sgqlc.types.Arg(SortDirection, graphql_name='direction', default='descending')),
        ('sort_field', sgqlc.types.Arg(MetricSorting, graphql_name='sortField', default=None)),
))
    )
    pagination_job = sgqlc.types.Field(sgqlc.types.non_null(JobPagination), graphql_name='paginationJob', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('sort', sgqlc.types.Arg(JobSorting, graphql_name='sort', default={'jobPendingSorting': {'sort': 'id', 'direction': 'descending'}, 'jobRunningSorting': {'sort': 'id', 'direction': 'descending'}, 'jobFinishedSorting': {'sort': 'id', 'direction': 'descending'}})),
        ('jobs_filter', sgqlc.types.Arg(JobsFilter, graphql_name='jobsFilter', default={})),
))
    )
    periodic_job = sgqlc.types.Field(sgqlc.types.non_null('PeriodicJob'), graphql_name='periodicJob', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    pagination_periodic_job = sgqlc.types.Field(sgqlc.types.non_null(PeriodicJobPagination), graphql_name='paginationPeriodicJob', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('filter_settings', sgqlc.types.Arg(PeriodicJobFilterSettings, graphql_name='filterSettings', default={})),
        ('sort_field', sgqlc.types.Arg(PeriodicJobSorting, graphql_name='sortField', default='id')),
        ('direction', sgqlc.types.Arg(SortDirection, graphql_name='direction', default='descending')),
))
    )
    pagination_periodic_job_logs = sgqlc.types.Field(sgqlc.types.non_null(PaginationLog), graphql_name='paginationPeriodicJobLogs', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('filter_settings', sgqlc.types.Arg(LogFilterSettings, graphql_name='filterSettings', default={})),
        ('direction', sgqlc.types.Arg(SortDirection, graphql_name='direction', default='descending')),
        ('sort_field', sgqlc.types.Arg(LogSorting, graphql_name='sortField', default=None)),
))
    )
    pagination_periodic_job_requests = sgqlc.types.Field(sgqlc.types.non_null(PaginationRequest), graphql_name='paginationPeriodicJobRequests', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('filter_settings', sgqlc.types.Arg(RequestFilterSettings, graphql_name='filterSettings', default={})),
        ('direction', sgqlc.types.Arg(SortDirection, graphql_name='direction', default='descending')),
        ('sort_field', sgqlc.types.Arg(RequestSorting, graphql_name='sortField', default=None)),
))
    )
    pagination_periodic_job_metrics = sgqlc.types.Field(sgqlc.types.non_null(PaginationMetric), graphql_name='paginationPeriodicJobMetrics', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('filter_settings', sgqlc.types.Arg(MetricFilterSettings, graphql_name='filterSettings', default={})),
        ('direction', sgqlc.types.Arg(SortDirection, graphql_name='direction', default='descending')),
        ('sort_field', sgqlc.types.Arg(MetricSorting, graphql_name='sortField', default=None)),
))
    )
    check_periodic_job_by_input = sgqlc.types.Field('PeriodicJob', graphql_name='checkPeriodicJobByInput', args=sgqlc.types.ArgDict((
        ('periodic_job_input', sgqlc.types.Arg(sgqlc.types.non_null(PeriodicJobInput), graphql_name='periodicJobInput', default=None)),
))
    )
    project = sgqlc.types.Field(sgqlc.types.non_null('Project'), graphql_name='project', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    pagination_project = sgqlc.types.Field(sgqlc.types.non_null(ProjectPagination), graphql_name='paginationProject', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('sort_field', sgqlc.types.Arg(ProjectSorting, graphql_name='sortField', default='id')),
        ('filter_settings', sgqlc.types.Arg(ProjectFilterSettings, graphql_name='filterSettings', default={})),
        ('direction', sgqlc.types.Arg(SortDirection, graphql_name='direction', default='descending')),
))
    )
    project_args_and_settings_description = sgqlc.types.Field(sgqlc.types.non_null(ArgsAndSettingsDescription), graphql_name='projectArgsAndSettingsDescription', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('version_id', sgqlc.types.Arg(ID, graphql_name='versionId', default=None)),
))
    )
    project_default_args_and_settings_description = sgqlc.types.Field(sgqlc.types.non_null(ArgsAndSettingsDescription), graphql_name='projectDefaultArgsAndSettingsDescription')
    information_source_loader = sgqlc.types.Field(sgqlc.types.non_null('InformationSourceLoader'), graphql_name='informationSourceLoader', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    pagination_information_source_loader = sgqlc.types.Field(sgqlc.types.non_null(PaginationInformationSourceLoader), graphql_name='paginationInformationSourceLoader', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('filter_settings', sgqlc.types.Arg(InformationSourceLoaderFilterSettings, graphql_name='filterSettings', default={})),
        ('sort_field', sgqlc.types.Arg(InformationSourceLoaderSorting, graphql_name='sortField', default='id')),
        ('direction', sgqlc.types.Arg(SortDirection, graphql_name='direction', default='descending')),
))
    )
    information_source = sgqlc.types.Field(sgqlc.types.non_null(InformationSource), graphql_name='informationSource', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    pagination_information_source = sgqlc.types.Field(sgqlc.types.non_null(PaginationInformationSource), graphql_name='paginationInformationSource', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('filter_settings', sgqlc.types.Arg(InformationSourceFilterSettings, graphql_name='filterSettings', default={})),
        ('sort_field', sgqlc.types.Arg(InformationSourceSorting, graphql_name='sortField', default='id')),
        ('direction', sgqlc.types.Arg(SortDirection, graphql_name='direction', default='descending')),
))
    )
    version = sgqlc.types.Field(sgqlc.types.non_null('Version'), graphql_name='version', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    list_version = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('Version')), graphql_name='listVersion', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids', default=None)),
))
    )
    pagination_versions_crawler = sgqlc.types.Field(sgqlc.types.non_null('VersionPagination'), graphql_name='paginationVersionsCrawler', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('filter_settings', sgqlc.types.Arg(VersionFilterSettings, graphql_name='filterSettings', default={'withRemovedVersions': False})),
        ('sort_field', sgqlc.types.Arg(VersionSorting, graphql_name='sortField', default='id')),
        ('direction', sgqlc.types.Arg(SortDirection, graphql_name='direction', default='descending')),
))
    )
    pagination_egg_file_versions_project = sgqlc.types.Field(sgqlc.types.non_null('VersionPagination'), graphql_name='paginationEggFileVersionsProject', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('with_removed', sgqlc.types.Arg(sgqlc.types.non_null(Boolean), graphql_name='withRemoved', default=False)),
        ('sort_field', sgqlc.types.Arg(VersionSorting, graphql_name='sortField', default='id')),
        ('direction', sgqlc.types.Arg(SortDirection, graphql_name='direction', default='descending')),
))
    )
    web_scraper_version_is_compatible = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='webScraperVersionIsCompatible', args=sgqlc.types.ArgDict((
        ('web_scraper_version', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='webScraperVersion', default=None)),
))
    )
    document = sgqlc.types.Field('Document', graphql_name='document', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    story = sgqlc.types.Field('Story', graphql_name='story', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids', default=None)),
))
    )
    pagination_story = sgqlc.types.Field(sgqlc.types.non_null('StoryPagination'), graphql_name='paginationStory', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('grouping', sgqlc.types.Arg(DocumentGrouping, graphql_name='grouping', default='none')),
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
        ('filter_settings', sgqlc.types.Arg(DocumentFilterSettings, graphql_name='filterSettings', default=None)),
        ('direction', sgqlc.types.Arg(SortDirection, graphql_name='direction', default='descending')),
        ('sort_field', sgqlc.types.Arg(DocumentSorting, graphql_name='sortField', default='score')),
        ('extra_settings', sgqlc.types.Arg(sgqlc.types.non_null(ExtraSettings), graphql_name='extraSettings', default=None)),
))
    )
    pagination_document_markers = sgqlc.types.Field(sgqlc.types.non_null(CommonStringPagination), graphql_name='paginationDocumentMarkers', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('direction', sgqlc.types.Arg(SortDirection, graphql_name='direction', default='descending')),
))
    )
    concept_type = sgqlc.types.Field(sgqlc.types.non_null('ConceptType'), graphql_name='conceptType', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    composite_concept_type = sgqlc.types.Field(sgqlc.types.non_null('CompositeConceptType'), graphql_name='compositeConceptType', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    pagination_composite_concept_type = sgqlc.types.Field(sgqlc.types.non_null(CompositeConceptTypePagination), graphql_name='paginationCompositeConceptType', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(CompositeConceptTypeFilterSettings), graphql_name='filterSettings', default=None)),
        ('direction', sgqlc.types.Arg(SortDirection, graphql_name='direction', default='descending')),
        ('sort_field', sgqlc.types.Arg(CompositeConceptTypeSorting, graphql_name='sortField', default='id')),
))
    )
    concept_property_type = sgqlc.types.Field(sgqlc.types.non_null('ConceptPropertyType'), graphql_name='conceptPropertyType', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    concept_link_type = sgqlc.types.Field(sgqlc.types.non_null('ConceptLinkType'), graphql_name='conceptLinkType', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    concept_property_value_type = sgqlc.types.Field(sgqlc.types.non_null('ConceptPropertyValueType'), graphql_name='conceptPropertyValueType', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    list_concept_type = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ConceptType'))), graphql_name='listConceptType')
    list_user_menu_type = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserMenuType'))), graphql_name='listUserMenuType')
    list_concept_property_type = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ConceptPropertyType'))), graphql_name='listConceptPropertyType')
    list_concept_property_type_by_id = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('ConceptPropertyType')), graphql_name='listConceptPropertyTypeById', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids', default=None)),
))
    )
    list_concept_link_type = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ConceptLinkType'))), graphql_name='listConceptLinkType')
    list_concept_property_value_type = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ConceptPropertyValueType'))), graphql_name='listConceptPropertyValueType')
    pagination_concept_type = sgqlc.types.Field(sgqlc.types.non_null(ConceptTypePagination), graphql_name='paginationConceptType', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(ConceptTypeFilterSettings), graphql_name='filterSettings', default=None)),
        ('direction', sgqlc.types.Arg(SortDirection, graphql_name='direction', default='descending')),
        ('sort_field', sgqlc.types.Arg(ConceptTypeSorting, graphql_name='sortField', default='id')),
))
    )
    pagination_concept_property_type = sgqlc.types.Field(sgqlc.types.non_null(ConceptPropertyTypePagination), graphql_name='paginationConceptPropertyType', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(ConceptPropertyTypeFilterSettings), graphql_name='filterSettings', default=None)),
        ('direction', sgqlc.types.Arg(SortDirection, graphql_name='direction', default='descending')),
        ('sort_field', sgqlc.types.Arg(ConceptPropertyTypeSorting, graphql_name='sortField', default='name')),
))
    )
    pagination_concept_link_property_type = sgqlc.types.Field(sgqlc.types.non_null(ConceptPropertyTypePagination), graphql_name='paginationConceptLinkPropertyType', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(ConceptPropertyTypeFilterSettings), graphql_name='filterSettings', default=None)),
        ('direction', sgqlc.types.Arg(SortDirection, graphql_name='direction', default='descending')),
        ('sort_field', sgqlc.types.Arg(ConceptPropertyTypeSorting, graphql_name='sortField', default='name')),
))
    )
    pagination_concept_link_type = sgqlc.types.Field(sgqlc.types.non_null(ConceptLinkTypePagination), graphql_name='paginationConceptLinkType', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(ConceptLinkTypeFilterSettings), graphql_name='filterSettings', default=None)),
        ('direction', sgqlc.types.Arg(SortDirection, graphql_name='direction', default='descending')),
        ('sort_field', sgqlc.types.Arg(ConceptLinkTypeSorting, graphql_name='sortField', default='id')),
))
    )
    pagination_concept_property_value_type = sgqlc.types.Field(sgqlc.types.non_null(ConceptPropertyValueTypePagination), graphql_name='paginationConceptPropertyValueType', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(ConceptPropertyValueTypeFilterSettings), graphql_name='filterSettings', default=None)),
        ('direction', sgqlc.types.Arg(SortDirection, graphql_name='direction', default='descending')),
        ('sort_field', sgqlc.types.Arg(ConceptPropertyValueTypeSorting, graphql_name='sortField', default='id')),
))
    )
    composite_concept_property_type = sgqlc.types.Field(sgqlc.types.non_null('ConceptPropertyType'), graphql_name='compositeConceptPropertyType', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    composite_link_property_type = sgqlc.types.Field(sgqlc.types.non_null('ConceptPropertyType'), graphql_name='compositeLinkPropertyType', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    list_composite_concept_property_type = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ConceptPropertyType'))), graphql_name='listCompositeConceptPropertyType')
    list_composite_link_property_type = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ConceptPropertyType'))), graphql_name='listCompositeLinkPropertyType')
    pagination_composite_concept_property_type = sgqlc.types.Field(sgqlc.types.non_null(ConceptPropertyTypePagination), graphql_name='paginationCompositeConceptPropertyType', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(CompositePropertyTypeFilterSettings), graphql_name='filterSettings', default=None)),
        ('direction', sgqlc.types.Arg(SortDirection, graphql_name='direction', default='descending')),
        ('sort_field', sgqlc.types.Arg(CompositePropertyTypeSorting, graphql_name='sortField', default='name')),
))
    )
    pagination_composite_link_property_type = sgqlc.types.Field(sgqlc.types.non_null(ConceptPropertyTypePagination), graphql_name='paginationCompositeLinkPropertyType', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(CompositePropertyTypeFilterSettings), graphql_name='filterSettings', default=None)),
        ('direction', sgqlc.types.Arg(SortDirection, graphql_name='direction', default='descending')),
        ('sort_field', sgqlc.types.Arg(CompositePropertyTypeSorting, graphql_name='sortField', default='name')),
))
    )
    composite_property_value_template = sgqlc.types.Field(sgqlc.types.non_null('CompositePropertyValueTemplate'), graphql_name='compositePropertyValueTemplate', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    list_composite_property_value_template = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('CompositePropertyValueTemplate'))), graphql_name='listCompositePropertyValueTemplate')
    pagination_composite_property_value_template = sgqlc.types.Field(sgqlc.types.non_null(CompositePropertyValueTemplatePagination), graphql_name='paginationCompositePropertyValueTemplate', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(CompositePropertyValueTemplateFilterSettings), graphql_name='filterSettings', default=None)),
        ('direction', sgqlc.types.Arg(SortDirection, graphql_name='direction', default='descending')),
        ('sort_field', sgqlc.types.Arg(CompositePropertyValueTemplateSorting, graphql_name='sortField', default='id')),
))
    )
    concept_type_view = sgqlc.types.Field(sgqlc.types.non_null('ConceptTypeView'), graphql_name='conceptTypeView', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    domain_map = sgqlc.types.Field(sgqlc.types.non_null(DomainMap), graphql_name='domainMap')
    concept = sgqlc.types.Field('Concept', graphql_name='concept', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    list_concept_by_id = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('Concept')), graphql_name='listConceptById', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids', default=None)),
))
    )
    pagination_concept = sgqlc.types.Field(ConceptPagination, graphql_name='paginationConcept', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
        ('filter_settings', sgqlc.types.Arg(ConceptFilterSettings, graphql_name='filterSettings', default=None)),
        ('direction', sgqlc.types.Arg(SortDirection, graphql_name='direction', default='descending')),
        ('sort_field', sgqlc.types.Arg(ConceptSorting, graphql_name='sortField', default='score')),
))
    )
    composite_concept = sgqlc.types.Field(sgqlc.types.non_null(CompositeConcept), graphql_name='compositeConcept', args=sgqlc.types.ArgDict((
        ('composite_concept_type_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='compositeConceptTypeId', default=None)),
        ('root_concept_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='rootConceptId', default=None)),
))
    )
    pagination_composite_concept = sgqlc.types.Field(sgqlc.types.non_null(CompositeConceptPagination), graphql_name='paginationCompositeConcept', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
        ('composite_concept_filter_settings', sgqlc.types.Arg(CompositeConceptFilterSettings, graphql_name='compositeConceptFilterSettings', default=None)),
        ('direction', sgqlc.types.Arg(SortDirection, graphql_name='direction', default='descending')),
        ('sort_field', sgqlc.types.Arg(ConceptSorting, graphql_name='sortField', default='score')),
))
    )
    list_concept_link_between_fixed_concepts = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ConceptLink'))), graphql_name='listConceptLinkBetweenFixedConcepts', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids', default=None)),
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(ConceptLinkFilterSettings), graphql_name='filterSettings', default=None)),
))
    )
    concept_property = sgqlc.types.Field('ConceptProperty', graphql_name='conceptProperty', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    concept_link = sgqlc.types.Field(sgqlc.types.non_null('ConceptLink'), graphql_name='conceptLink', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    pagination_concept_link = sgqlc.types.Field(sgqlc.types.non_null(ConceptLinkPagination), graphql_name='paginationConceptLink', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(ConceptLinkFilterSettings), graphql_name='filterSettings', default=None)),
))
    )
    pagination_kbrelated_document = sgqlc.types.Field(DocumentPagination, graphql_name='paginationKBRelatedDocument', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(RelatedDocumentFilterSettings), graphql_name='filterSettings', default=None)),
        ('direction', sgqlc.types.Arg(SortDirection, graphql_name='direction', default='descending')),
        ('sort_field', sgqlc.types.Arg(RelatedDocumentSorting, graphql_name='sortField', default='registrationDate')),
))
    )
    issue = sgqlc.types.Field('Issue', graphql_name='issue', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    pagination_issue = sgqlc.types.Field(IssuePagination, graphql_name='paginationIssue', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(IssueFilterSettings), graphql_name='filterSettings', default=None)),
        ('direction', sgqlc.types.Arg(SortDirection, graphql_name='direction', default='descending')),
        ('sort_field', sgqlc.types.Arg(IssueSorting, graphql_name='sortField', default='id')),
))
    )
    pagination_issue_change = sgqlc.types.Field(sgqlc.types.non_null(IssueChangePagination), graphql_name='paginationIssueChange', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
))
    )
    research_map = sgqlc.types.Field(sgqlc.types.non_null('ResearchMap'), graphql_name='researchMap', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    pagination_research_map = sgqlc.types.Field(sgqlc.types.non_null('ResearchMapPagination'), graphql_name='paginationResearchMap', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(ResearchMapFilterSettings), graphql_name='filterSettings', default=None)),
        ('direction', sgqlc.types.Arg(SortDirection, graphql_name='direction', default='descending')),
        ('sort_field', sgqlc.types.Arg(ResearchMapSorting, graphql_name='sortField', default='id')),
))
    )
    active_research_map = sgqlc.types.Field('ResearchMap', graphql_name='activeResearchMap')
    list_top_neighbors_on_map = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ConceptWithNeighbors))), graphql_name='listTopNeighborsOnMap', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(ResearchMapContentSelectInput), graphql_name='form', default=None)),
        ('quantity', sgqlc.types.Arg(Int, graphql_name='quantity', default=10)),
))
    )
    list_last_research_map = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ResearchMap'))), graphql_name='listLastResearchMap')
    document_autocomplete = sgqlc.types.Field(sgqlc.types.non_null(Autocomplete), graphql_name='documentAutocomplete', args=sgqlc.types.ArgDict((
        ('destination', sgqlc.types.Arg(sgqlc.types.non_null(AutocompleteDocumentDestination), graphql_name='destination', default=None)),
        ('query', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='query', default=None)),
))
    )
    concept_autocomplete = sgqlc.types.Field(sgqlc.types.non_null(Autocomplete), graphql_name='conceptAutocomplete', args=sgqlc.types.ArgDict((
        ('destination', sgqlc.types.Arg(sgqlc.types.non_null(AutocompleteConceptDestination), graphql_name='destination', default=None)),
        ('query', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='query', default=None)),
))
    )
    get_osm_place_name = sgqlc.types.Field(sgqlc.types.non_null(GeoPointValue), graphql_name='getOsmPlaceName', args=sgqlc.types.ArgDict((
        ('latitude', sgqlc.types.Arg(sgqlc.types.non_null(Float), graphql_name='latitude', default=None)),
        ('longitude', sgqlc.types.Arg(sgqlc.types.non_null(Float), graphql_name='longitude', default=None)),
))
    )
    get_osm_coordinates = sgqlc.types.Field(sgqlc.types.non_null(GeoPointValue), graphql_name='getOsmCoordinates', args=sgqlc.types.ArgDict((
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
))
    )
    access_level = sgqlc.types.Field(sgqlc.types.non_null(AccessLevel), graphql_name='accessLevel', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    pagination_access_level = sgqlc.types.Field(sgqlc.types.non_null(AccessLevelPagination), graphql_name='paginationAccessLevel', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('direction', sgqlc.types.Arg(SortDirection, graphql_name='direction', default='descending')),
        ('sort_field', sgqlc.types.Arg(AccessLevelSorting, graphql_name='sortField', default='id')),
))
    )
    story_fs2_query = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='storyFs2Query', args=sgqlc.types.ArgDict((
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(DocumentFilterSettings), graphql_name='filterSettings', default=None)),
        ('extra_settings', sgqlc.types.Arg(sgqlc.types.non_null(ExtraSettings), graphql_name='extraSettings', default=None)),
))
    )
    concept_fs2_query = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='conceptFs2Query', args=sgqlc.types.ArgDict((
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(ConceptFilterSettings), graphql_name='filterSettings', default=None)),
))
    )
    markers_bulk = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(Markers)), graphql_name='markersBulk', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(BulkMarkersInput), graphql_name='form', default=None)),
))
    )
    platform = sgqlc.types.Field(sgqlc.types.non_null('Platform'), graphql_name='platform', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    list_platform_by_id = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Platform'))), graphql_name='listPlatformById', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids', default=None)),
))
    )
    pagination_platform = sgqlc.types.Field(sgqlc.types.non_null(PlatformPagination), graphql_name='paginationPlatform', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(PlatformFilterSettings), graphql_name='filterSettings', default=None)),
        ('direction', sgqlc.types.Arg(SortDirection, graphql_name='direction', default='descending')),
        ('sort_field', sgqlc.types.Arg(PlatformSorting, graphql_name='sortField', default='id')),
))
    )
    account = sgqlc.types.Field(sgqlc.types.non_null('Account'), graphql_name='account', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    list_account_by_id = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Account'))), graphql_name='listAccountById', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids', default=None)),
))
    )
    pagination_account = sgqlc.types.Field(sgqlc.types.non_null(AccountPagination), graphql_name='paginationAccount', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(AccountFilterSettings), graphql_name='filterSettings', default=None)),
        ('direction', sgqlc.types.Arg(SortDirection, graphql_name='direction', default='descending')),
        ('sort_field', sgqlc.types.Arg(AccountSorting, graphql_name='sortField', default='id')),
))
    )
    pagination_country = sgqlc.types.Field(sgqlc.types.non_null(CountryPagination), graphql_name='paginationCountry', args=sgqlc.types.ArgDict((
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(CountryFilterSettings), graphql_name='filterSettings', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
))
    )
    pagination_language = sgqlc.types.Field(sgqlc.types.non_null(LanguagePagination), graphql_name='paginationLanguage', args=sgqlc.types.ArgDict((
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(LanguageFilterSettings), graphql_name='filterSettings', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
))
    )
    document_feed = sgqlc.types.Field(sgqlc.types.non_null('DocumentFeed'), graphql_name='documentFeed', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    pagination_document_feed = sgqlc.types.Field(sgqlc.types.non_null(DocumentFeedPagination), graphql_name='paginationDocumentFeed', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(DocumentFeedFilterSettings), graphql_name='filterSettings', default=None)),
        ('direction', sgqlc.types.Arg(SortDirection, graphql_name='direction', default='descending')),
        ('sort_field', sgqlc.types.Arg(DocumentFeedSorting, graphql_name='sortField', default='id')),
))
    )
    concept_registry_view = sgqlc.types.Field(sgqlc.types.non_null(ConceptRegistryView), graphql_name='conceptRegistryView')
    document_registry_view = sgqlc.types.Field(sgqlc.types.non_null(DocumentRegistryView), graphql_name='documentRegistryView')
    document_card_view = sgqlc.types.Field(sgqlc.types.non_null(DocumentCardView), graphql_name='documentCardView')
    chart = sgqlc.types.Field(sgqlc.types.non_null(Chart), graphql_name='chart', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    preview_chart = sgqlc.types.Field(sgqlc.types.non_null(Chart), graphql_name='previewChart', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(ChartDescriptionInput), graphql_name='form', default=None)),
))
    )
    pipeline_transforms = sgqlc.types.Field(sgqlc.types.non_null(PipelineTransformList), graphql_name='pipelineTransforms', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('filter', sgqlc.types.Arg(PipelineTransformFilter, graphql_name='filter', default=None)),
))
    )
    pipeline_transform = sgqlc.types.Field(sgqlc.types.non_null(PipelineTransform), graphql_name='pipelineTransform', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    pipeline_configs = sgqlc.types.Field(sgqlc.types.non_null(PipelineConfigList), graphql_name='pipelineConfigs', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('filter', sgqlc.types.Arg(PipelineConfigFilter, graphql_name='filter', default=None)),
        ('sort_by', sgqlc.types.Arg(PipelineConfigSort, graphql_name='sortBy', default='id')),
        ('sort_direction', sgqlc.types.Arg(SortDirection, graphql_name='sortDirection', default='ascending')),
))
    )
    pipeline_config = sgqlc.types.Field(sgqlc.types.non_null('PipelineConfig'), graphql_name='pipelineConfig', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    export_pipeline_config = sgqlc.types.Field(sgqlc.types.non_null(JSON), graphql_name='exportPipelineConfig', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    kafka_pipeline_start_type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='kafkaPipelineStartType')
    kafka_topics = sgqlc.types.Field(sgqlc.types.non_null(KafkaTopicList), graphql_name='kafkaTopics', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('filter', sgqlc.types.Arg(KafkaTopicFilter, graphql_name='filter', default=None)),
        ('sort_by', sgqlc.types.Arg(KafkaTopicSort, graphql_name='sortBy', default='topic')),
        ('sort_direction', sgqlc.types.Arg(SortDirection, graphql_name='sortDirection', default='ascending')),
))
    )
    kafka_topic = sgqlc.types.Field(sgqlc.types.non_null('KafkaTopic'), graphql_name='kafkaTopic', args=sgqlc.types.ArgDict((
        ('topic', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='topic', default=None)),
))
    )
    message_status = sgqlc.types.Field(sgqlc.types.non_null(MessageStatus), graphql_name='messageStatus', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    message_topic = sgqlc.types.Field(ID, graphql_name='messageTopic', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    message_statuses = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(MessageStatus))), graphql_name='messageStatuses', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids', default=None)),
))
    )
    failed_messages = sgqlc.types.Field(sgqlc.types.non_null(FailedMessageList), graphql_name='failedMessages', args=sgqlc.types.ArgDict((
        ('topic', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='topic', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('sort_by', sgqlc.types.Arg(MessageSort, graphql_name='sortBy', default='timestamp')),
        ('sort_direction', sgqlc.types.Arg(SortDirection, graphql_name='sortDirection', default='descending')),
        ('filter', sgqlc.types.Arg(MessageFilter, graphql_name='filter', default=None)),
))
    )
    pending_messages = sgqlc.types.Field(sgqlc.types.non_null(PendingMessageList), graphql_name='pendingMessages', args=sgqlc.types.ArgDict((
        ('topic', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='topic', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('sort_by', sgqlc.types.Arg(ItemsSort, graphql_name='sortBy', default='timestamp')),
        ('sort_direction', sgqlc.types.Arg(SortDirection, graphql_name='sortDirection', default='descending')),
        ('filter', sgqlc.types.Arg(MessageFilter, graphql_name='filter', default=None)),
))
    )
    active_messages = sgqlc.types.Field(sgqlc.types.non_null(ActiveMessageList), graphql_name='activeMessages', args=sgqlc.types.ArgDict((
        ('topic', sgqlc.types.Arg(ID, graphql_name='topic', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('sort_by', sgqlc.types.Arg(ItemsSort, graphql_name='sortBy', default='timestamp')),
        ('sort_direction', sgqlc.types.Arg(SortDirection, graphql_name='sortDirection', default='descending')),
        ('filter', sgqlc.types.Arg(MessageFilter, graphql_name='filter', default=None)),
))
    )
    completed_ok_messages = sgqlc.types.Field(sgqlc.types.non_null(CompletedOkMessageList), graphql_name='completedOkMessages', args=sgqlc.types.ArgDict((
        ('topic', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='topic', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('sort_by', sgqlc.types.Arg(MessageSort, graphql_name='sortBy', default='timestamp')),
        ('sort_direction', sgqlc.types.Arg(SortDirection, graphql_name='sortDirection', default='descending')),
        ('filter', sgqlc.types.Arg(MessageFilter, graphql_name='filter', default=None)),
))
    )
    duplicate_messages = sgqlc.types.Field(sgqlc.types.non_null(DuplicateMessageList), graphql_name='duplicateMessages', args=sgqlc.types.ArgDict((
        ('topic', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='topic', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('sort_by', sgqlc.types.Arg(MessageSort, graphql_name='sortBy', default='timestamp')),
        ('sort_direction', sgqlc.types.Arg(SortDirection, graphql_name='sortDirection', default='descending')),
        ('filter', sgqlc.types.Arg(MessageFilter, graphql_name='filter', default=None)),
))
    )
    messages_by_parent_id = sgqlc.types.Field(sgqlc.types.non_null(MessageList), graphql_name='messagesByParentId', args=sgqlc.types.ArgDict((
        ('parent_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='parentId', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('sort_by', sgqlc.types.Arg(ItemsSort, graphql_name='sortBy', default='timestamp')),
        ('sort_direction', sgqlc.types.Arg(SortDirection, graphql_name='sortDirection', default='descending')),
        ('filter', sgqlc.types.Arg(MessageFilter, graphql_name='filter', default=None)),
))
    )
    exporter = sgqlc.types.Field(sgqlc.types.non_null('Exporter'), graphql_name='exporter', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    exporters = sgqlc.types.Field(sgqlc.types.non_null(ExporterList), graphql_name='exporters', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('sort_by', sgqlc.types.Arg(ExporterSort, graphql_name='sortBy', default='id')),
        ('sort_direction', sgqlc.types.Arg(SortDirection, graphql_name='sortDirection', default='ascending')),
        ('filter', sgqlc.types.Arg(ExporterFilter, graphql_name='filter', default=None)),
))
    )
    export_task = sgqlc.types.Field(sgqlc.types.non_null('ExportTask'), graphql_name='exportTask', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    export_tasks = sgqlc.types.Field(sgqlc.types.non_null(ExportTaskList), graphql_name='exportTasks', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('sort_by', sgqlc.types.Arg(ExportTaskSort, graphql_name='sortBy', default='createTime')),
        ('sort_direction', sgqlc.types.Arg(SortDirection, graphql_name='sortDirection', default='descending')),
        ('filter', sgqlc.types.Arg(ExportTaskFilter, graphql_name='filter', default=None)),
))
    )
    job_items2 = sgqlc.types.Field(sgqlc.types.non_null(ItemsList), graphql_name='jobItems2', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('items_filter', sgqlc.types.Arg(ItemsFilter, graphql_name='itemsFilter', default={'inputText': None, 'interval': None, 'topic': None})),
        ('items_sort', sgqlc.types.Arg(ItemsSort, graphql_name='itemsSort', default='timestamp')),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=10)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('sort_direction', sgqlc.types.Arg(SortDirection, graphql_name='sortDirection', default='descending')),
))
    )
    periodic_job_items2 = sgqlc.types.Field(sgqlc.types.non_null(ItemsList), graphql_name='periodicJobItems2', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('items_filter', sgqlc.types.Arg(ItemsFilter, graphql_name='itemsFilter', default={'inputText': None, 'interval': None, 'topic': None})),
        ('items_sort', sgqlc.types.Arg(ItemsSort, graphql_name='itemsSort', default='timestamp')),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=10)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('sort_direction', sgqlc.types.Arg(SortDirection, graphql_name='sortDirection', default='descending')),
))
    )
    task_items2 = sgqlc.types.Field(sgqlc.types.non_null(ItemsList), graphql_name='taskItems2', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('items_filter', sgqlc.types.Arg(ItemsFilter, graphql_name='itemsFilter', default={'inputText': None, 'interval': None, 'topic': None})),
        ('items_sort', sgqlc.types.Arg(ItemsSort, graphql_name='itemsSort', default='timestamp')),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=10)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('sort_direction', sgqlc.types.Arg(SortDirection, graphql_name='sortDirection', default='descending')),
))
    )
    periodic_task_items2 = sgqlc.types.Field(sgqlc.types.non_null(ItemsList), graphql_name='periodicTaskItems2', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('items_filter', sgqlc.types.Arg(ItemsFilter, graphql_name='itemsFilter', default={'inputText': None, 'interval': None, 'topic': None})),
        ('items_sort', sgqlc.types.Arg(ItemsSort, graphql_name='itemsSort', default='timestamp')),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=10)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('sort_direction', sgqlc.types.Arg(SortDirection, graphql_name='sortDirection', default='descending')),
))
    )
    job_ids_by_message_uuid2 = sgqlc.types.Field(JobIds, graphql_name='jobIdsByMessageUUID2', args=sgqlc.types.ArgDict((
        ('message_uuid', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='messageUUID', default=None)),
))
    )
    job_metrics2 = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(JobMetrics))), graphql_name='jobMetrics2', args=sgqlc.types.ArgDict((
        ('job_ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='jobIds', default=None)),
))
    )
    periodic_job_metrics2 = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(PeriodicJobMetrics))), graphql_name='periodicJobMetrics2', args=sgqlc.types.ArgDict((
        ('periodic_job_ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='periodicJobIds', default=None)),
))
    )
    task_metrics2 = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TaskMetrics'))), graphql_name='taskMetrics2', args=sgqlc.types.ArgDict((
        ('task_ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='taskIds', default=None)),
))
    )
    periodic_task_metrics2 = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(PeriodicTaskMetrics))), graphql_name='periodicTaskMetrics2', args=sgqlc.types.ArgDict((
        ('periodic_task_ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='periodicTaskIds', default=None)),
))
    )
    concept_transform_configs = sgqlc.types.Field(sgqlc.types.non_null(ConceptTransformConfigList), graphql_name='conceptTransformConfigs', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('filter', sgqlc.types.Arg(ConceptTransformConfigFilter, graphql_name='filter', default=None)),
        ('sort_by', sgqlc.types.Arg(ConceptTransformConfigSort, graphql_name='sortBy', default='id')),
        ('sort_direction', sgqlc.types.Arg(SortDirection, graphql_name='sortDirection', default='ascending')),
))
    )
    concept_transform_config = sgqlc.types.Field(sgqlc.types.non_null('ConceptTransformConfig'), graphql_name='conceptTransformConfig', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    concept_transform_message_type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='conceptTransformMessageType')
    concept_transform_task = sgqlc.types.Field(sgqlc.types.non_null('ConceptTransformTask'), graphql_name='conceptTransformTask', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    concept_transform_tasks = sgqlc.types.Field(sgqlc.types.non_null(ConceptTransformTaskList), graphql_name='conceptTransformTasks', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('sort_by', sgqlc.types.Arg(ConceptTransformTaskSort, graphql_name='sortBy', default='createTime')),
        ('sort_direction', sgqlc.types.Arg(SortDirection, graphql_name='sortDirection', default='descending')),
        ('filter', sgqlc.types.Arg(ConceptTransformTaskFilter, graphql_name='filter', default=None)),
))
    )
    user_pipeline_transforms = sgqlc.types.Field(sgqlc.types.non_null('UserPipelineTransformList'), graphql_name='userPipelineTransforms', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('sort_by', sgqlc.types.Arg(UserPipelineTransformSort, graphql_name='sortBy', default='id')),
        ('sort_direction', sgqlc.types.Arg(SortDirection, graphql_name='sortDirection', default='descending')),
        ('filter', sgqlc.types.Arg(UserPipelineTransformFilter, graphql_name='filter', default=None)),
))
    )
    user_pipeline_transform = sgqlc.types.Field(sgqlc.types.non_null('UserPipelineTransform'), graphql_name='userPipelineTransform', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    user = sgqlc.types.Field('User', graphql_name='user', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    current_user = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='currentUser')
    pagination_user = sgqlc.types.Field(sgqlc.types.non_null('UserPagination'), graphql_name='paginationUser', args=sgqlc.types.ArgDict((
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(UserFilterSettings), graphql_name='filterSettings', default=None)),
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
))
    )
    get_kvstore_item = sgqlc.types.Field(String, graphql_name='getKVStoreItem', args=sgqlc.types.ArgDict((
        ('key', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='key', default=None)),
))
    )
    pagination_attribute = sgqlc.types.Field(sgqlc.types.non_null(AttributePagination), graphql_name='paginationAttribute', args=sgqlc.types.ArgDict((
        ('attribute_filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(AttributeFilterSettings), graphql_name='attributeFilterSettings', default=None)),
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
))
    )
    user_group = sgqlc.types.Field(sgqlc.types.non_null('UserGroup'), graphql_name='userGroup', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    pagination_user_group = sgqlc.types.Field(sgqlc.types.non_null('UserGroupPagination'), graphql_name='paginationUserGroup', args=sgqlc.types.ArgDict((
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(UserGroupFilterSettings), graphql_name='filterSettings', default=None)),
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
))
    )
    event = sgqlc.types.Field(sgqlc.types.non_null(Event), graphql_name='event', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    pagination_event = sgqlc.types.Field(sgqlc.types.non_null(EventPagination), graphql_name='paginationEvent', args=sgqlc.types.ArgDict((
        ('event_filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(EventFilterSettings), graphql_name='eventFilterSettings', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
))
    )
    list_external_search_jobs_by_job_ids = sgqlc.types.Field(sgqlc.types.list_of('ExternalSearch'), graphql_name='listExternalSearchJobsByJobIds', args=sgqlc.types.ArgDict((
        ('search_job_ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='searchJobIds', default=None)),
))
    )
    list_external_search_tasks_by_task_ids = sgqlc.types.Field(sgqlc.types.list_of('ExternalSearch'), graphql_name='listExternalSearchTasksByTaskIds', args=sgqlc.types.ArgDict((
        ('search_task_ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='searchTaskIds', default=None)),
))
    )
    pagination_external_search = sgqlc.types.Field(PaginationExternalSearch, graphql_name='paginationExternalSearch', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='offset', default=0)),
        ('sort_field', sgqlc.types.Arg(sgqlc.types.non_null(ExternalSearchJobSorting), graphql_name='sortField', default='ID')),
        ('direction', sgqlc.types.Arg(sgqlc.types.non_null(SortDirection), graphql_name='direction', default=None)),
        ('target', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(SearchTarget))), graphql_name='target', default=())),
        ('concept_ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='conceptIds', default=None)),
))
    )
    pagination_noisy_jobs_by_primary_job = sgqlc.types.Field(PaginationJob, graphql_name='paginationNoisyJobsByPrimaryJob', args=sgqlc.types.ArgDict((
        ('search_job_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='searchJobId', default=None)),
        ('limit', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='offset', default=None)),
        ('sort_field', sgqlc.types.Arg(sgqlc.types.non_null(ExternalSearchJobSorting), graphql_name='sortField', default=None)),
        ('direction', sgqlc.types.Arg(sgqlc.types.non_null(SortDirection), graphql_name='direction', default=None)),
))
    )
    list_search_objects_of_concept = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('SearchObject')), graphql_name='listSearchObjectsOfConcept', args=sgqlc.types.ArgDict((
        ('concept_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='conceptId', default=None)),
))
    )
    search_object = sgqlc.types.Field('SearchObject', graphql_name='searchObject', args=sgqlc.types.ArgDict((
        ('search_object_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='searchObjectId', default=None)),
))
    )
    search_object_with_nested = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('SearchObject')), graphql_name='searchObjectWithNested', args=sgqlc.types.ArgDict((
        ('search_object_ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='searchObjectIds', default=None)),
))
    )
    list_search_objects = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('SearchObject')), graphql_name='listSearchObjects', args=sgqlc.types.ArgDict((
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(SearchObjectFilterSettingsInput), graphql_name='filterSettings', default=None)),
        ('sorting', sgqlc.types.Arg(sgqlc.types.non_null(SearchObjectsSortingInput), graphql_name='sorting', default=None)),
))
    )
    pagination_search_objects = sgqlc.types.Field(PaginationSearchObject, graphql_name='paginationSearchObjects', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='offset', default=None)),
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(SearchObjectFilterSettingsInput), graphql_name='filterSettings', default=None)),
        ('sorting', sgqlc.types.Arg(sgqlc.types.non_null(SearchObjectsSortingInput), graphql_name='sorting', default=None)),
))
    )
    name_autocomplete = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='nameAutocomplete', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='query', default=None)),
        ('limit', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='limit', default=5)),
))
    )
    noisy_file = sgqlc.types.Field(NoisyFile, graphql_name='noisyFile', args=sgqlc.types.ArgDict((
        ('noisy_file_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='noisyFileId', default=None)),
))
    )
    noisy_file_by_concept_property_type_id = sgqlc.types.Field(NoisyFile, graphql_name='noisyFileByConceptPropertyTypeId', args=sgqlc.types.ArgDict((
        ('concept_property_type_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='conceptPropertyTypeId', default=None)),
))
    )
    noisy_file_content = sgqlc.types.Field(sgqlc.types.list_of(NoisyFileContent), graphql_name='noisyFileContent', args=sgqlc.types.ArgDict((
        ('concept_property_type_ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='conceptPropertyTypeIds', default=None)),
))
    )
    language = sgqlc.types.Field(Language, graphql_name='language', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    language_list_by_id = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(Language)), graphql_name='languageListById', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids', default=None)),
))
    )
    detect_language = sgqlc.types.Field(sgqlc.types.non_null(Language), graphql_name='detectLanguage', args=sgqlc.types.ArgDict((
        ('text', sgqlc.types.Arg(String, graphql_name='text', default=None)),
))
    )
    translate_str = sgqlc.types.Field(String, graphql_name='translateStr', args=sgqlc.types.ArgDict((
        ('text', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='text', default=None)),
        ('source', sgqlc.types.Arg(ID, graphql_name='source', default=None)),
        ('target', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='target', default=None)),
))
    )
    source_languages = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Language))), graphql_name='sourceLanguages')
    default_language = sgqlc.types.Field(Language, graphql_name='defaultLanguage')


class RecordInterface(sgqlc.types.Interface):
    __schema__ = api_schema_new
    __field_names__ = ('system_registration_date', 'system_update_date', 'creator', 'last_updater')
    system_registration_date = sgqlc.types.Field(sgqlc.types.non_null(UnixTime), graphql_name='systemRegistrationDate')
    system_update_date = sgqlc.types.Field(UnixTime, graphql_name='systemUpdateDate')
    creator = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='creator')
    last_updater = sgqlc.types.Field('User', graphql_name='lastUpdater')


class RelExtModel(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('source_annotation_type', 'target_annotation_type', 'relation_type', 'invert_direction')
    source_annotation_type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='sourceAnnotationType')
    target_annotation_type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='targetAnnotationType')
    relation_type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='relationType')
    invert_direction = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='invertDirection')


class ReportConfig(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('report_export_result',)
    report_export_result = sgqlc.types.Field(String, graphql_name='reportExportResult')


class Request(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('job_id', 'timestamp', 'last_seen', 'url', 'request_url', 'fingerprint', 'method', 'http_status', 'response_size', 'duration')
    job_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='jobId')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(UnixTime), graphql_name='timestamp')
    last_seen = sgqlc.types.Field(sgqlc.types.non_null(UnixTime), graphql_name='lastSeen')
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')
    request_url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='requestUrl')
    fingerprint = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='fingerprint')
    method = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='method')
    http_status = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='httpStatus')
    response_size = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='responseSize')
    duration = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='duration')


class ResearchMapChangedEvent(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('event_name', 'research_map')
    event_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='eventName')
    research_map = sgqlc.types.Field(sgqlc.types.non_null('ResearchMap'), graphql_name='researchMap')


class ResearchMapFromFilesType(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('research_maps', 'info')
    research_maps = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ResearchMap'))), graphql_name='researchMaps')
    info = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('State')), graphql_name='info')


class ResearchMapPagination(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('total', 'list_research_map')
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')
    list_research_map = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ResearchMap'))), graphql_name='listResearchMap')


class ResearchMapStatistics(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('object_num', 'event_num', 'document_num', 'concept_num', 'concept_and_document_num')
    object_num = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='objectNum')
    event_num = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='eventNum')
    document_num = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='documentNum')
    concept_num = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='conceptNum')
    concept_and_document_num = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='conceptAndDocumentNum')


class SearchQuery(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('query', 'concept_id')
    query = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='query')
    concept_id = sgqlc.types.Field(ID, graphql_name='conceptId')


class ServiceStats(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('name', 'duration', 'load', 'ok_requests', 'failed_requests')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    duration = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='duration')
    load = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='load')
    ok_requests = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='okRequests')
    failed_requests = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='failedRequests')


class SettingDescription(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('name', 'type', 'short_description', 'long_description', 'required', 'default')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    type = sgqlc.types.Field(sgqlc.types.non_null(SettingsType), graphql_name='type')
    short_description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='shortDescription')
    long_description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='longDescription')
    required = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='required')
    default = sgqlc.types.Field(String, graphql_name='default')


class SoftwareChartFilterSettings(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('name', 'date_interval', 'soft_types')
    name = sgqlc.types.Field(String, graphql_name='name')
    date_interval = sgqlc.types.Field(DateTimeInterval, graphql_name='dateInterval')
    soft_types = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='softTypes')


class SoftwareVuln(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('concept', 'soft_type', 'median_value', 'total_vuln', 'delta', 'history')
    concept = sgqlc.types.Field(sgqlc.types.non_null('Concept'), graphql_name='concept')
    soft_type = sgqlc.types.Field(String, graphql_name='softType')
    median_value = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='medianValue')
    total_vuln = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalVuln')
    delta = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='delta')
    history = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(CountDateValue)), graphql_name='history')


class SoftwareVulnObject(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('soft_vuln', 'max_history_value', 'history_count', 'next_date')
    soft_vuln = sgqlc.types.Field(sgqlc.types.non_null(SoftwareVuln), graphql_name='softVuln')
    max_history_value = sgqlc.types.Field(Int, graphql_name='maxHistoryValue')
    history_count = sgqlc.types.Field(Int, graphql_name='historyCount')
    next_date = sgqlc.types.Field(String, graphql_name='nextDate')


class State(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('is_success',)
    is_success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isSuccess')


class StateWithError(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('state', 'info')
    state = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='state')
    info = sgqlc.types.Field(sgqlc.types.non_null(ConflictsState), graphql_name='info')


class Stats(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('type_of_stats', 'user_id', 'jobs_metrics', 'items_histogram', 'projects_histogram', 'previous_items_histogram')
    type_of_stats = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='typeOfStats')
    user_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='userId')
    jobs_metrics = sgqlc.types.Field(sgqlc.types.non_null(JobStats), graphql_name='jobsMetrics', args=sgqlc.types.ArgDict((
        ('interval', sgqlc.types.Arg(TimestampInterval, graphql_name='interval', default=None)),
))
    )
    items_histogram = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(DateHistogramBucket))), graphql_name='itemsHistogram', args=sgqlc.types.ArgDict((
        ('interval', sgqlc.types.Arg(TimestampInterval, graphql_name='interval', default=None)),
))
    )
    projects_histogram = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ProjectHistogram))), graphql_name='projectsHistogram', args=sgqlc.types.ArgDict((
        ('interval', sgqlc.types.Arg(TimestampInterval, graphql_name='interval', default=None)),
))
    )
    previous_items_histogram = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(DateHistogramBucket))), graphql_name='previousItemsHistogram', args=sgqlc.types.ArgDict((
        ('interval', sgqlc.types.Arg(TimestampInterval, graphql_name='interval', default=None)),
))
    )


class Story(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('id', 'title', 'system_registration_date', 'system_update_date', 'main', 'list_document', 'highlighting', 'count_doc', 'preview', 'access_level')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    title = sgqlc.types.Field(String, graphql_name='title')
    system_registration_date = sgqlc.types.Field(sgqlc.types.non_null(UnixTime), graphql_name='systemRegistrationDate')
    system_update_date = sgqlc.types.Field(UnixTime, graphql_name='systemUpdateDate')
    main = sgqlc.types.Field(sgqlc.types.non_null('Document'), graphql_name='main')
    list_document = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Document'))), graphql_name='listDocument')
    highlighting = sgqlc.types.Field(Highlighting, graphql_name='highlighting')
    count_doc = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='countDoc')
    preview = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='preview')
    access_level = sgqlc.types.Field(sgqlc.types.non_null(AccessLevel), graphql_name='accessLevel')


class StoryPagination(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('list_story', 'total', 'show_total', 'list_named_entity_count_facet', 'list_concept_count_facet', 'list_account_count_facet', 'list_platform_count_facet', 'list_markers', 'sources', 'new_documents_today')
    list_story = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Story))), graphql_name='listStory')
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')
    show_total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='showTotal')
    list_named_entity_count_facet = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Facet))), graphql_name='listNamedEntityCountFacet')
    list_concept_count_facet = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Facet))), graphql_name='listConceptCountFacet')
    list_account_count_facet = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AccountFacet))), graphql_name='listAccountCountFacet')
    list_platform_count_facet = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(PlatformFacet))), graphql_name='listPlatformCountFacet')
    list_markers = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Facet))), graphql_name='listMarkers')
    sources = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='sources')
    new_documents_today = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='newDocumentsToday')


class StringLocaleValue(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('value', 'locale')
    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='value')
    locale = sgqlc.types.Field(sgqlc.types.non_null(Locale), graphql_name='locale')


class StringValue(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('value',)
    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='value')


class Subscription(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('research_map_changed', 'event')
    research_map_changed = sgqlc.types.Field(sgqlc.types.non_null(ResearchMapChangedEvent), graphql_name='researchMapChanged', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    event = sgqlc.types.Field(sgqlc.types.non_null(Event), graphql_name='event')


class Table(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('cells', 'metadata')
    cells = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))))), graphql_name='cells')
    metadata = sgqlc.types.Field(sgqlc.types.non_null('TableMetadata'), graphql_name='metadata')


class TableMetadata(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('page_id',)
    page_id = sgqlc.types.Field(Int, graphql_name='pageId')


class TaskImportMetrics(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('errors_count',)
    errors_count = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='errorsCount')


class TaskList(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('pending', 'running', 'finished')
    pending = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Task'))), graphql_name='pending')
    running = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Task'))), graphql_name='running')
    finished = sgqlc.types.Field(sgqlc.types.non_null('TaskPagination'), graphql_name='finished')


class TaskMetrics(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('task_id', 'metrics')
    task_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='taskId')
    metrics = sgqlc.types.Field(sgqlc.types.non_null(MessageMetrics), graphql_name='metrics')


class TaskPagination(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('total', 'tasks')
    total = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='total')
    tasks = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Task'))), graphql_name='tasks')


class TaskPanel(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('filter_id',)
    filter_id = sgqlc.types.Field(ID, graphql_name='filterId')


class TextBounding(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('start', 'end', 'node_id')
    start = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='start')
    end = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='end')
    node_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='nodeId')


class Time(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('hour', 'minute', 'second')
    hour = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='hour')
    minute = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='minute')
    second = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='second')


class Translation(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('text', 'language')
    text = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='text')
    language = sgqlc.types.Field(sgqlc.types.non_null(Language), graphql_name='language')


class UpdateDashboard(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('is_success', 'dashboard')
    is_success = sgqlc.types.Field(Boolean, graphql_name='isSuccess')
    dashboard = sgqlc.types.Field(Dashboard, graphql_name='dashboard')


class UpdateDashboardLayout(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('is_success', 'layout')
    is_success = sgqlc.types.Field(Boolean, graphql_name='isSuccess')
    layout = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(DashboardLayoutItem))), graphql_name='layout')


class UpdateDashboardPanel(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('is_success',)
    is_success = sgqlc.types.Field(Boolean, graphql_name='isSuccess')


class UpdateProjectStats(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('added_crawlers_count', 'deleted_crawlers_count', 'updated_crawlers_count', 'is_metadata_updated', 'updated_periodic_ids', 'stopped_periodic_ids')
    added_crawlers_count = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='addedCrawlersCount')
    deleted_crawlers_count = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='deletedCrawlersCount')
    updated_crawlers_count = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='updatedCrawlersCount')
    is_metadata_updated = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isMetadataUpdated')
    updated_periodic_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Long))), graphql_name='updatedPeriodicIds')
    stopped_periodic_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Long))), graphql_name='stoppedPeriodicIds')


class UserAttribute(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('id', 'name', 'json_value')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    json_value = sgqlc.types.Field(sgqlc.types.non_null(JSON), graphql_name='jsonValue')


class UserGroupMetrics(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('count_user',)
    count_user = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='countUser')


class UserGroupPagination(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('list_user_group', 'total')
    list_user_group = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserGroup'))), graphql_name='listUserGroup')
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')


class UserGroupWithError(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('user_group', 'info')
    user_group = sgqlc.types.Field(sgqlc.types.non_null('UserGroup'), graphql_name='userGroup')
    info = sgqlc.types.Field(sgqlc.types.non_null(ConflictsState), graphql_name='info')


class UserMetrics(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('count_group',)
    count_group = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='countGroup')


class UserPagination(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('list_user', 'total')
    list_user = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('User'))), graphql_name='listUser')
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')


class UserPipelineTransformList(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('transforms', 'total')
    transforms = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserPipelineTransform'))), graphql_name='transforms')
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')


class UserService(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('mem_limit', 'mem_request', 'cpu_limit', 'cpu_request', 'max_pods', 'state', 'environment')
    mem_limit = sgqlc.types.Field(Int, graphql_name='memLimit')
    mem_request = sgqlc.types.Field(Int, graphql_name='memRequest')
    cpu_limit = sgqlc.types.Field(Int, graphql_name='cpuLimit')
    cpu_request = sgqlc.types.Field(Int, graphql_name='cpuRequest')
    max_pods = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='maxPods')
    state = sgqlc.types.Field(sgqlc.types.non_null(UserServiceState), graphql_name='state')
    environment = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('UserServiceEnvironmentVariable')), graphql_name='environment')


class UserServiceEnvironmentVariable(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('name', 'value')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='value')


class UserWithError(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('user', 'info')
    user = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='user')
    info = sgqlc.types.Field(sgqlc.types.non_null(ConflictsState), graphql_name='info')


class VersionData(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('id', 'version_name', 'status')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    version_name = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='versionName')
    status = sgqlc.types.Field(sgqlc.types.non_null(VersionStatus), graphql_name='status')


class VersionPagination(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('total', 'list_version')
    total = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='total')
    list_version = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Version'))), graphql_name='listVersion')


class VulnChartFilterSettings(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('name', 'date_interval', 'integral', 'cvss3')
    name = sgqlc.types.Field(String, graphql_name='name')
    date_interval = sgqlc.types.Field(DateTimeInterval, graphql_name='dateInterval')
    integral = sgqlc.types.Field(IntervalIntValue, graphql_name='integral')
    cvss3 = sgqlc.types.Field(IntervalIntValue, graphql_name='cvss3')


class Vulnerability(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('concept', 'cvss3', 'publication_date', 'software_list', 'exploit_amount', 'integral', 'mentions_amount', 'delta', 'history', 'severity_class')
    concept = sgqlc.types.Field(sgqlc.types.non_null('Concept'), graphql_name='concept')
    cvss3 = sgqlc.types.Field(Float, graphql_name='cvss3')
    publication_date = sgqlc.types.Field(Date, graphql_name='publicationDate')
    software_list = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('Concept')), graphql_name='softwareList')
    exploit_amount = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='exploitAmount')
    integral = sgqlc.types.Field(Int, graphql_name='integral')
    mentions_amount = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='mentionsAmount')
    delta = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='delta')
    history = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(CountDateValue)), graphql_name='history')
    severity_class = sgqlc.types.Field(sgqlc.types.non_null(SeverityCategories), graphql_name='severityClass')


class VulnerabilityObject(sgqlc.types.Type):
    __schema__ = api_schema_new
    __field_names__ = ('vuln', 'max_history_value', 'history_count', 'next_date')
    vuln = sgqlc.types.Field(sgqlc.types.non_null(Vulnerability), graphql_name='vuln')
    max_history_value = sgqlc.types.Field(Int, graphql_name='maxHistoryValue')
    history_count = sgqlc.types.Field(Int, graphql_name='historyCount')
    next_date = sgqlc.types.Field(String, graphql_name='nextDate')


class Account(sgqlc.types.Type, RecordInterface):
    __schema__ = api_schema_new
    __field_names__ = ('id', 'name', 'url', 'country', 'markers', 'params', 'platform', 'image', 'metric', 'period')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')
    country = sgqlc.types.Field(String, graphql_name='country')
    markers = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='markers')
    params = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Parameter))), graphql_name='params')
    platform = sgqlc.types.Field(sgqlc.types.non_null('Platform'), graphql_name='platform')
    image = sgqlc.types.Field(Image, graphql_name='image')
    metric = sgqlc.types.Field(sgqlc.types.non_null(AccountStatistics), graphql_name='metric')
    period = sgqlc.types.Field(sgqlc.types.non_null(DateTimeInterval), graphql_name='period')


class CompositeConceptType(sgqlc.types.Type, RecordInterface):
    __schema__ = api_schema_new
    __field_names__ = ('id', 'name', 'root_concept_type', 'is_default', 'layout', 'has_supporting_documents', 'has_header_information', 'metric', 'pagination_widget_type', 'list_widget_type', 'list_concept_link_types_composite_concept_type_consists_of', 'show_in_menu')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    root_concept_type = sgqlc.types.Field(sgqlc.types.non_null('ConceptType'), graphql_name='rootConceptType')
    is_default = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isDefault')
    layout = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='layout')
    has_supporting_documents = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasSupportingDocuments')
    has_header_information = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasHeaderInformation')
    metric = sgqlc.types.Field(sgqlc.types.non_null(CompositeConceptStatistics), graphql_name='metric')
    pagination_widget_type = sgqlc.types.Field(sgqlc.types.non_null(CompositeConceptTypeWidgetTypePagination), graphql_name='paginationWidgetType', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('sort_direction', sgqlc.types.Arg(SortDirection, graphql_name='sortDirection', default='ascending')),
        ('sorting', sgqlc.types.Arg(CompositeConceptTypeWidgetTypeSorting, graphql_name='sorting', default='order')),
))
    )
    list_widget_type = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('CompositeConceptTypeWidgetType'))), graphql_name='listWidgetType')
    list_concept_link_types_composite_concept_type_consists_of = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ConceptLinkType'))), graphql_name='listConceptLinkTypesCompositeConceptTypeConsistsOf')
    show_in_menu = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='showInMenu')


class CompositeConceptTypeWidgetType(sgqlc.types.Type, RecordInterface):
    __schema__ = api_schema_new
    __field_names__ = ('id', 'name', 'table_type', 'composite_concept_type', 'hierarchy', 'columns_info')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    table_type = sgqlc.types.Field(sgqlc.types.non_null(WidgetTypeTableType), graphql_name='tableType')
    composite_concept_type = sgqlc.types.Field(sgqlc.types.non_null(CompositeConceptType), graphql_name='compositeConceptType')
    hierarchy = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ConceptLinkTypePath))))), graphql_name='hierarchy')
    columns_info = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CompositeConceptTypeWidgetTypeColumn))), graphql_name='columnsInfo')


class CompositePropertyValueTemplate(sgqlc.types.Type, RecordInterface):
    __schema__ = api_schema_new
    __field_names__ = ('id', 'name', 'component_value_types')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    component_value_types = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CompositePropertyValueType))), graphql_name='componentValueTypes')


class Concept(sgqlc.types.Type, RecordInterface):
    __schema__ = api_schema_new
    __field_names__ = ('id', 'is_actual', 'name', 'notes', 'markers', 'start_date', 'end_date', 'concept_type', 'pagination_concept_property', 'pagination_concept_link', 'pagination_concept_fact', 'pagination_concept_property_documents', 'pagination_concept_link_documents', 'list_concept_fact', 'image', 'metric', 'list_alias', 'pagination_alias', 'pagination_merged_concept', 'list_header_concept_property', 'pagination_issue', 'access_level', 'list_subscription', 'pagination_research_map')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    is_actual = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isActual')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    notes = sgqlc.types.Field(String, graphql_name='notes')
    markers = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='markers')
    start_date = sgqlc.types.Field(DateTimeValue, graphql_name='startDate')
    end_date = sgqlc.types.Field(DateTimeValue, graphql_name='endDate')
    concept_type = sgqlc.types.Field(sgqlc.types.non_null('ConceptType'), graphql_name='conceptType')
    pagination_concept_property = sgqlc.types.Field(sgqlc.types.non_null(ConceptPropertyPagination), graphql_name='paginationConceptProperty', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(ConceptPropertyFilterSettings), graphql_name='filterSettings', default=None)),
))
    )
    pagination_concept_link = sgqlc.types.Field(sgqlc.types.non_null(ConceptLinkPagination), graphql_name='paginationConceptLink', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(ConceptLinkFilterSettings), graphql_name='filterSettings', default=None)),
))
    )
    pagination_concept_fact = sgqlc.types.Field(sgqlc.types.non_null(ConceptFactPagination), graphql_name='paginationConceptFact', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(DocumentLinkFilterSetting), graphql_name='filterSettings', default=None)),
))
    )
    pagination_concept_property_documents = sgqlc.types.Field(sgqlc.types.non_null(DocumentPagination), graphql_name='paginationConceptPropertyDocuments', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(ConceptPropertyFilterSettings), graphql_name='filterSettings', default=None)),
))
    )
    pagination_concept_link_documents = sgqlc.types.Field(sgqlc.types.non_null(DocumentPagination), graphql_name='paginationConceptLinkDocuments', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(ConceptLinkFilterSettings), graphql_name='filterSettings', default=None)),
))
    )
    list_concept_fact = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ConceptFact'))), graphql_name='listConceptFact')
    image = sgqlc.types.Field(Image, graphql_name='image')
    metric = sgqlc.types.Field(sgqlc.types.non_null(ConceptStatistics), graphql_name='metric')
    list_alias = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ConceptProperty'))), graphql_name='listAlias')
    pagination_alias = sgqlc.types.Field(sgqlc.types.non_null(ConceptPropertyPagination), graphql_name='paginationAlias', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
))
    )
    pagination_merged_concept = sgqlc.types.Field(sgqlc.types.non_null(MergedConceptPagination), graphql_name='paginationMergedConcept', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
))
    )
    list_header_concept_property = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ConceptProperty'))), graphql_name='listHeaderConceptProperty')
    pagination_issue = sgqlc.types.Field(sgqlc.types.non_null(IssuePagination), graphql_name='paginationIssue', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(IssueFilterSettings), graphql_name='filterSettings', default=None)),
        ('sort_direction', sgqlc.types.Arg(sgqlc.types.non_null(SortDirection), graphql_name='sortDirection', default=None)),
        ('sorting', sgqlc.types.Arg(sgqlc.types.non_null(IssueSorting), graphql_name='sorting', default=None)),
))
    )
    access_level = sgqlc.types.Field(sgqlc.types.non_null(AccessLevel), graphql_name='accessLevel')
    list_subscription = sgqlc.types.Field(sgqlc.types.non_null(ConceptSubscriptions), graphql_name='listSubscription')
    pagination_research_map = sgqlc.types.Field(sgqlc.types.non_null(ResearchMapPagination), graphql_name='paginationResearchMap', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(ResearchMapFilterSettings), graphql_name='filterSettings', default=None)),
        ('sort_direction', sgqlc.types.Arg(sgqlc.types.non_null(SortDirection), graphql_name='sortDirection', default=None)),
        ('sorting', sgqlc.types.Arg(sgqlc.types.non_null(ResearchMapSorting), graphql_name='sorting', default=None)),
))
    )


class ConceptCandidateFact(sgqlc.types.Type, FactInterface):
    __schema__ = api_schema_new
    __field_names__ = ('name', 'concept_type', 'list_concept')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    concept_type = sgqlc.types.Field(sgqlc.types.non_null('ConceptType'), graphql_name='conceptType')
    list_concept = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Concept))), graphql_name='listConcept')


class ConceptFact(sgqlc.types.Type, FactInterface, RecordInterface):
    __schema__ = api_schema_new
    __field_names__ = ('access_level', 'concept')
    access_level = sgqlc.types.Field(sgqlc.types.non_null(AccessLevel), graphql_name='accessLevel')
    concept = sgqlc.types.Field(sgqlc.types.non_null(Concept), graphql_name='concept')


class ConceptLink(sgqlc.types.Type, RecordInterface):
    __schema__ = api_schema_new
    __field_names__ = ('id', 'concept_from_id', 'concept_to_id', 'notes', 'start_date', 'end_date', 'concept_from', 'concept_to', 'concept_link_type', 'pagination_concept_link_property', 'pagination_concept_link_property_documents', 'pagination_document', 'list_concept_link_fact', 'access_level')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    concept_from_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='conceptFromId')
    concept_to_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='conceptToId')
    notes = sgqlc.types.Field(String, graphql_name='notes')
    start_date = sgqlc.types.Field(DateTimeValue, graphql_name='startDate')
    end_date = sgqlc.types.Field(DateTimeValue, graphql_name='endDate')
    concept_from = sgqlc.types.Field(sgqlc.types.non_null(Concept), graphql_name='conceptFrom')
    concept_to = sgqlc.types.Field(sgqlc.types.non_null(Concept), graphql_name='conceptTo')
    concept_link_type = sgqlc.types.Field(sgqlc.types.non_null('ConceptLinkType'), graphql_name='conceptLinkType')
    pagination_concept_link_property = sgqlc.types.Field(sgqlc.types.non_null(ConceptPropertyPagination), graphql_name='paginationConceptLinkProperty', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(ConceptPropertyFilterSettings), graphql_name='filterSettings', default=None)),
))
    )
    pagination_concept_link_property_documents = sgqlc.types.Field(sgqlc.types.non_null(DocumentPagination), graphql_name='paginationConceptLinkPropertyDocuments', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(ConceptPropertyFilterSettings), graphql_name='filterSettings', default=None)),
))
    )
    pagination_document = sgqlc.types.Field(sgqlc.types.non_null(DocumentPagination), graphql_name='paginationDocument', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
))
    )
    list_concept_link_fact = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ConceptLinkFact'))), graphql_name='listConceptLinkFact')
    access_level = sgqlc.types.Field(sgqlc.types.non_null(AccessLevel), graphql_name='accessLevel')


class ConceptLinkCandidateFact(sgqlc.types.Type, FactInterface):
    __schema__ = api_schema_new
    __field_names__ = ('concept_link_type', 'fact_from', 'fact_to')
    concept_link_type = sgqlc.types.Field(sgqlc.types.non_null('ConceptLinkType'), graphql_name='conceptLinkType')
    fact_from = sgqlc.types.Field('ConceptLikeFact', graphql_name='factFrom')
    fact_to = sgqlc.types.Field('ConceptLikeFact', graphql_name='factTo')


class ConceptLinkFact(sgqlc.types.Type, FactInterface, RecordInterface):
    __schema__ = api_schema_new
    __field_names__ = ('access_level', 'concept_link')
    access_level = sgqlc.types.Field(sgqlc.types.non_null(AccessLevel), graphql_name='accessLevel')
    concept_link = sgqlc.types.Field(sgqlc.types.non_null(ConceptLink), graphql_name='conceptLink')


class ConceptLinkPropertyFact(sgqlc.types.Type, FactInterface, RecordInterface):
    __schema__ = api_schema_new
    __field_names__ = ('parent_concept_link', 'access_level', 'concept_link_property')
    parent_concept_link = sgqlc.types.Field(sgqlc.types.non_null(ConceptLink), graphql_name='parentConceptLink')
    access_level = sgqlc.types.Field(sgqlc.types.non_null(AccessLevel), graphql_name='accessLevel')
    concept_link_property = sgqlc.types.Field(sgqlc.types.non_null('ConceptProperty'), graphql_name='conceptLinkProperty')


class ConceptLinkType(sgqlc.types.Type, RecordInterface):
    __schema__ = api_schema_new
    __field_names__ = ('id', 'name', 'is_directed', 'is_hierarchical', 'concept_from_type', 'concept_to_type', 'pretrained_rel_ext_models', 'notify_on_update', 'pagination_concept_link_property_type', 'list_concept_link_property_type', 'metric')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    is_directed = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isDirected')
    is_hierarchical = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isHierarchical')
    concept_from_type = sgqlc.types.Field(sgqlc.types.non_null('ConceptType'), graphql_name='conceptFromType')
    concept_to_type = sgqlc.types.Field(sgqlc.types.non_null('ConceptType'), graphql_name='conceptToType')
    pretrained_rel_ext_models = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(RelExtModel))), graphql_name='pretrainedRelExtModels')
    notify_on_update = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='notifyOnUpdate')
    pagination_concept_link_property_type = sgqlc.types.Field(sgqlc.types.non_null(ConceptPropertyTypePagination), graphql_name='paginationConceptLinkPropertyType', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(ConceptPropertyTypeFilterSettings), graphql_name='filterSettings', default=None)),
        ('sort_direction', sgqlc.types.Arg(sgqlc.types.non_null(SortDirection), graphql_name='sortDirection', default=None)),
        ('sorting', sgqlc.types.Arg(sgqlc.types.non_null(ConceptTypeSorting), graphql_name='sorting', default=None)),
))
    )
    list_concept_link_property_type = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ConceptPropertyType'))), graphql_name='listConceptLinkPropertyType')
    metric = sgqlc.types.Field(sgqlc.types.non_null(ConceptLinkTypeStatistics), graphql_name='metric')


class ConceptProperty(sgqlc.types.Type, RecordInterface):
    __schema__ = api_schema_new
    __field_names__ = ('id', 'is_main', 'property_type', 'notes', 'start_date', 'end_date', 'pagination_document', 'access_level', 'value', 'list_concept_property_fact')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    is_main = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isMain')
    property_type = sgqlc.types.Field(sgqlc.types.non_null('ConceptPropertyType'), graphql_name='propertyType')
    notes = sgqlc.types.Field(String, graphql_name='notes')
    start_date = sgqlc.types.Field(DateTimeValue, graphql_name='startDate')
    end_date = sgqlc.types.Field(DateTimeValue, graphql_name='endDate')
    pagination_document = sgqlc.types.Field(sgqlc.types.non_null(DocumentPagination), graphql_name='paginationDocument', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
))
    )
    access_level = sgqlc.types.Field(sgqlc.types.non_null(AccessLevel), graphql_name='accessLevel')
    value = sgqlc.types.Field(sgqlc.types.non_null('AnyValue'), graphql_name='value')
    list_concept_property_fact = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ConceptPropertyLikeFact'))), graphql_name='listConceptPropertyFact')


class ConceptPropertyCandidateFact(sgqlc.types.Type, FactInterface):
    __schema__ = api_schema_new
    __field_names__ = ('concept_property_type', 'fact_to', 'fact_from')
    concept_property_type = sgqlc.types.Field(sgqlc.types.non_null('ConceptPropertyType'), graphql_name='conceptPropertyType')
    fact_to = sgqlc.types.Field(sgqlc.types.non_null('ConceptPropertyValueCandidateFact'), graphql_name='factTo')
    fact_from = sgqlc.types.Field('ConceptLikeFact', graphql_name='factFrom')


class ConceptPropertyFact(sgqlc.types.Type, FactInterface, RecordInterface):
    __schema__ = api_schema_new
    __field_names__ = ('parent_concept', 'access_level', 'concept_property')
    parent_concept = sgqlc.types.Field(sgqlc.types.non_null(Concept), graphql_name='parentConcept')
    access_level = sgqlc.types.Field(sgqlc.types.non_null(AccessLevel), graphql_name='accessLevel')
    concept_property = sgqlc.types.Field(sgqlc.types.non_null(ConceptProperty), graphql_name='conceptProperty')


class ConceptPropertyType(sgqlc.types.Type, RecordInterface):
    __schema__ = api_schema_new
    __field_names__ = ('id', 'name', 'pretrained_rel_ext_models', 'notify_on_update', 'computable_formula', 'parent_concept_type', 'parent_concept_link_type', 'value_type')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    pretrained_rel_ext_models = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(RelExtModel))), graphql_name='pretrainedRelExtModels')
    notify_on_update = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='notifyOnUpdate')
    computable_formula = sgqlc.types.Field(String, graphql_name='computableFormula')
    parent_concept_type = sgqlc.types.Field('ConceptType', graphql_name='parentConceptType')
    parent_concept_link_type = sgqlc.types.Field(ConceptLinkType, graphql_name='parentConceptLinkType')
    value_type = sgqlc.types.Field(sgqlc.types.non_null('AnyValueType'), graphql_name='valueType')


class ConceptPropertyValueCandidateFact(sgqlc.types.Type, FactInterface):
    __schema__ = api_schema_new
    __field_names__ = ('concept_property_value_type',)
    concept_property_value_type = sgqlc.types.Field(sgqlc.types.non_null('ConceptPropertyValueType'), graphql_name='conceptPropertyValueType')


class ConceptPropertyValueType(sgqlc.types.Type, RecordInterface):
    __schema__ = api_schema_new
    __field_names__ = ('id', 'name', 'value_type', 'list_white_dictionary', 'pretrained_nercmodels', 'list_white_regexp', 'value_restriction', 'list_black_dictionary', 'metric', 'list_concept_type', 'pagination_concept_type', 'list_concept_link_type', 'pagination_concept_link_type', 'list_black_regexp', 'list_type_search_element', 'list_type_black_search_element')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    value_type = sgqlc.types.Field(sgqlc.types.non_null(ValueType), graphql_name='valueType')
    list_white_dictionary = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='listWhiteDictionary')
    pretrained_nercmodels = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='pretrainedNERCModels')
    list_white_regexp = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(NERCRegexp))), graphql_name='listWhiteRegexp')
    value_restriction = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='valueRestriction')
    list_black_dictionary = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='listBlackDictionary')
    metric = sgqlc.types.Field(sgqlc.types.non_null(ConceptPropertyValueStatistics), graphql_name='metric')
    list_concept_type = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ConceptType'))), graphql_name='listConceptType')
    pagination_concept_type = sgqlc.types.Field(sgqlc.types.non_null(ConceptTypePagination), graphql_name='paginationConceptType', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
))
    )
    list_concept_link_type = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ConceptLinkType))), graphql_name='listConceptLinkType')
    pagination_concept_link_type = sgqlc.types.Field(sgqlc.types.non_null(ConceptLinkTypePagination), graphql_name='paginationConceptLinkType', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
))
    )
    list_black_regexp = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(NERCRegexp))), graphql_name='listBlackRegexp')
    list_type_search_element = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TypeSearchElement'))), graphql_name='listTypeSearchElement')
    list_type_black_search_element = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TypeSearchElement'))), graphql_name='listTypeBlackSearchElement')


class ConceptTransformConfig(sgqlc.types.Type, RecordInterface):
    __schema__ = api_schema_new
    __field_names__ = ('id', 'title', 'description', 'concept_type_ids', 'can_transform_one_entity', 'can_transform_multiple_entities', 'transforms', 'last_task_time', 'metrics', 'priority', 'deleted')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    description = sgqlc.types.Field(String, graphql_name='description')
    concept_type_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='conceptTypeIds')
    can_transform_one_entity = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='canTransformOneEntity')
    can_transform_multiple_entities = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='canTransformMultipleEntities')
    transforms = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(PipelineTransformSetup))), graphql_name='transforms')
    last_task_time = sgqlc.types.Field(UnixTime, graphql_name='lastTaskTime')
    metrics = sgqlc.types.Field(sgqlc.types.non_null(KafkaTopicMetrics), graphql_name='metrics')
    priority = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='priority')
    deleted = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleted')


class ConceptTransformTask(sgqlc.types.Type, RecordInterface):
    __schema__ = api_schema_new
    __field_names__ = ('id', 'concept_ids', 'state', 'active', 'result', 'config')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    concept_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='conceptIds')
    state = sgqlc.types.Field(sgqlc.types.non_null(ConceptTransformTaskState), graphql_name='state')
    active = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='active')
    result = sgqlc.types.Field(ConceptTransformResults, graphql_name='result')
    config = sgqlc.types.Field(ConceptTransformConfig, graphql_name='config')


class ConceptType(sgqlc.types.Type, RecordInterface):
    __schema__ = api_schema_new
    __field_names__ = ('id', 'name', 'x_coordinate', 'y_coordinate', 'list_white_dictionary', 'pretrained_nercmodels', 'list_white_regexp', 'is_event', 'list_black_dictionary', 'pagination_concept_property_type', 'metric', 'pagination_concept_link_type', 'pagination_concept_type_view', 'list_composite_concept_type', 'list_concept_property_type', 'list_concept_link_type', 'list_concept_header_property_type', 'image', 'non_configurable_dictionary', 'show_in_menu', 'list_black_regexp', 'list_names_dictionary', 'list_type_search_element', 'list_type_black_search_element')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    x_coordinate = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='xCoordinate')
    y_coordinate = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='yCoordinate')
    list_white_dictionary = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='listWhiteDictionary')
    pretrained_nercmodels = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='pretrainedNERCModels')
    list_white_regexp = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(NERCRegexp))), graphql_name='listWhiteRegexp')
    is_event = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isEvent')
    list_black_dictionary = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='listBlackDictionary')
    pagination_concept_property_type = sgqlc.types.Field(sgqlc.types.non_null(ConceptPropertyTypePagination), graphql_name='paginationConceptPropertyType', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(ConceptPropertyTypeFilterSettings), graphql_name='filterSettings', default=None)),
        ('sort_direction', sgqlc.types.Arg(SortDirection, graphql_name='sortDirection', default='descending')),
        ('sorting', sgqlc.types.Arg(ConceptPropertyTypeSorting, graphql_name='sorting', default='name')),
))
    )
    metric = sgqlc.types.Field(sgqlc.types.non_null(ConceptTypeStatistics), graphql_name='metric')
    pagination_concept_link_type = sgqlc.types.Field(sgqlc.types.non_null(ConceptLinkTypePagination), graphql_name='paginationConceptLinkType', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(ConceptLinkTypeFilterSettings), graphql_name='filterSettings', default=None)),
        ('sort_direction', sgqlc.types.Arg(SortDirection, graphql_name='sortDirection', default='descending')),
        ('sorting', sgqlc.types.Arg(ConceptLinkTypeSorting, graphql_name='sorting', default='id')),
))
    )
    pagination_concept_type_view = sgqlc.types.Field(sgqlc.types.non_null(ConceptTypeViewPagination), graphql_name='paginationConceptTypeView', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
))
    )
    list_composite_concept_type = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CompositeConceptType))), graphql_name='listCompositeConceptType')
    list_concept_property_type = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ConceptPropertyType))), graphql_name='listConceptPropertyType')
    list_concept_link_type = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ConceptLinkType))), graphql_name='listConceptLinkType')
    list_concept_header_property_type = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ConceptPropertyType))), graphql_name='listConceptHeaderPropertyType')
    image = sgqlc.types.Field(Image, graphql_name='image')
    non_configurable_dictionary = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='nonConfigurableDictionary')
    show_in_menu = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='showInMenu')
    list_black_regexp = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(NERCRegexp))), graphql_name='listBlackRegexp')
    list_names_dictionary = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='listNamesDictionary')
    list_type_search_element = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TypeSearchElement'))), graphql_name='listTypeSearchElement')
    list_type_black_search_element = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TypeSearchElement'))), graphql_name='listTypeBlackSearchElement')


class ConceptTypeView(sgqlc.types.Type, RecordInterface):
    __schema__ = api_schema_new
    __field_names__ = ('id', 'name', 'show_in_menu', 'concept_type', 'columns', 'pagination_concept')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    show_in_menu = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='showInMenu')
    concept_type = sgqlc.types.Field(sgqlc.types.non_null(ConceptType), graphql_name='conceptType')
    columns = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CompositeConceptTypeWidgetTypeColumn))), graphql_name='columns')
    pagination_concept = sgqlc.types.Field(sgqlc.types.non_null(ConceptViewPagination), graphql_name='paginationConcept', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('sort_column', sgqlc.types.Arg(ID, graphql_name='sortColumn', default=None)),
        ('sort_direction', sgqlc.types.Arg(SortDirection, graphql_name='sortDirection', default='descending')),
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
        ('filter_settings', sgqlc.types.Arg(ConceptFilterSettings, graphql_name='filterSettings', default=None)),
))
    )


class Crawler(sgqlc.types.Type, RecordInterface):
    __schema__ = api_schema_new
    __field_names__ = ('id', 'name', 'title', 'description', 'project', 'periodic_jobs_num', 'onetime_jobs_num', 'last_collection_date', 'state_version', 'avg_performance_time', 'pinned', 'settings', 'args', 'state', 'analytics', 'histogram_items', 'histogram_requests', 'job_stats', 'current_version', 'start_urls', 'sitemap')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    description = sgqlc.types.Field(String, graphql_name='description')
    project = sgqlc.types.Field(sgqlc.types.non_null(ProjectData), graphql_name='project')
    periodic_jobs_num = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='periodicJobsNum')
    onetime_jobs_num = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='onetimeJobsNum')
    last_collection_date = sgqlc.types.Field(Long, graphql_name='lastCollectionDate')
    state_version = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='stateVersion')
    avg_performance_time = sgqlc.types.Field(Float, graphql_name='avgPerformanceTime')
    pinned = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='pinned')
    settings = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(KeyValue))), graphql_name='settings')
    args = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(KeyValue))), graphql_name='args')
    state = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(KeyValue))), graphql_name='state')
    analytics = sgqlc.types.Field(sgqlc.types.non_null(CrawlerStats), graphql_name='analytics', args=sgqlc.types.ArgDict((
        ('interval', sgqlc.types.Arg(TimestampInterval, graphql_name='interval', default=None)),
))
    )
    histogram_items = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(DateHistogramBucket))), graphql_name='histogramItems', args=sgqlc.types.ArgDict((
        ('interval', sgqlc.types.Arg(TimestampInterval, graphql_name='interval', default=None)),
))
    )
    histogram_requests = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(DateHistogramBucket))), graphql_name='histogramRequests', args=sgqlc.types.ArgDict((
        ('interval', sgqlc.types.Arg(TimestampInterval, graphql_name='interval', default=None)),
))
    )
    job_stats = sgqlc.types.Field(sgqlc.types.non_null(JobStats), graphql_name='jobStats', args=sgqlc.types.ArgDict((
        ('interval', sgqlc.types.Arg(TimestampInterval, graphql_name='interval', default=None)),
))
    )
    current_version = sgqlc.types.Field('Version', graphql_name='currentVersion')
    start_urls = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='startUrls')
    sitemap = sgqlc.types.Field(JSON, graphql_name='sitemap')


class Credential(sgqlc.types.Type, RecordInterface):
    __schema__ = api_schema_new
    __field_names__ = ('id', 'data_type', 'description', 'login', 'password', 'token', 'domain', 'projects', 'status', 'state', 'cookies', 'version')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    data_type = sgqlc.types.Field(sgqlc.types.non_null(CredentialType), graphql_name='dataType')
    description = sgqlc.types.Field(String, graphql_name='description')
    login = sgqlc.types.Field(String, graphql_name='login')
    password = sgqlc.types.Field(String, graphql_name='password')
    token = sgqlc.types.Field(String, graphql_name='token')
    domain = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='domain')
    projects = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ProjectData))), graphql_name='projects')
    status = sgqlc.types.Field(sgqlc.types.non_null(CredentialStatus), graphql_name='status')
    state = sgqlc.types.Field(JSON, graphql_name='state')
    cookies = sgqlc.types.Field(JSON, graphql_name='cookies')
    version = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='version')


class Document(sgqlc.types.Type, RecordInterface):
    __schema__ = api_schema_new
    __field_names__ = ('id', 'title', 'external_url', 'publication_date', 'publication_author', 'notes', 'document_type', 'highlightings', 'markers', 'tables', 'metadata', 'uuid', 'trust_level', 'score', 'has_text', 'parent', 'list_child', 'pagination_child', 'internal_url', 'avatar', 'metric', 'pagination_concept_fact', 'list_concept_fact', 'pagination_concept_link_fact', 'list_concept_link_document_fact', 'preview', 'pagination_issue', 'access_level', 'text', 'story', 'list_subscription', 'pagination_similar_documents', 'is_read', 'list_fact')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    title = sgqlc.types.Field(String, graphql_name='title')
    external_url = sgqlc.types.Field(String, graphql_name='externalUrl')
    publication_date = sgqlc.types.Field(UnixTime, graphql_name='publicationDate')
    publication_author = sgqlc.types.Field(String, graphql_name='publicationAuthor')
    notes = sgqlc.types.Field(String, graphql_name='notes')
    document_type = sgqlc.types.Field(sgqlc.types.non_null(DocumentType), graphql_name='documentType')
    highlightings = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Highlighting))), graphql_name='highlightings')
    markers = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='markers')
    tables = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Table))), graphql_name='tables')
    metadata = sgqlc.types.Field(DocumentMetadata, graphql_name='metadata')
    uuid = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='uuid')
    trust_level = sgqlc.types.Field(TrustLevel, graphql_name='trustLevel')
    score = sgqlc.types.Field(Float, graphql_name='score')
    has_text = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasText')
    parent = sgqlc.types.Field('Document', graphql_name='parent')
    list_child = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Document'))), graphql_name='listChild')
    pagination_child = sgqlc.types.Field(sgqlc.types.non_null(DocumentPagination), graphql_name='paginationChild', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(DocumentLinkFilterSetting), graphql_name='filterSettings', default=None)),
))
    )
    internal_url = sgqlc.types.Field(String, graphql_name='internalUrl')
    avatar = sgqlc.types.Field(Image, graphql_name='avatar')
    metric = sgqlc.types.Field(sgqlc.types.non_null(Metrics), graphql_name='metric')
    pagination_concept_fact = sgqlc.types.Field(sgqlc.types.non_null(ConceptFactPagination), graphql_name='paginationConceptFact', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
))
    )
    list_concept_fact = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ConceptFact))), graphql_name='listConceptFact')
    pagination_concept_link_fact = sgqlc.types.Field(sgqlc.types.non_null(ConceptLinkFactPagination), graphql_name='paginationConceptLinkFact', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
))
    )
    list_concept_link_document_fact = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ConceptLinkFact))), graphql_name='listConceptLinkDocumentFact')
    preview = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='preview')
    pagination_issue = sgqlc.types.Field(sgqlc.types.non_null(IssuePagination), graphql_name='paginationIssue', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(IssueFilterSettings), graphql_name='filterSettings', default=None)),
        ('sort_direction', sgqlc.types.Arg(sgqlc.types.non_null(SortDirection), graphql_name='sortDirection', default=None)),
        ('sorting', sgqlc.types.Arg(sgqlc.types.non_null(IssueSorting), graphql_name='sorting', default=None)),
))
    )
    access_level = sgqlc.types.Field(sgqlc.types.non_null(AccessLevel), graphql_name='accessLevel')
    text = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(FlatDocumentStructure))), graphql_name='text', args=sgqlc.types.ArgDict((
        ('show_hidden', sgqlc.types.Arg(Boolean, graphql_name='showHidden', default=False)),
))
    )
    story = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='story')
    list_subscription = sgqlc.types.Field(sgqlc.types.non_null(DocumentSubscriptions), graphql_name='listSubscription')
    pagination_similar_documents = sgqlc.types.Field(sgqlc.types.non_null(DocumentPagination), graphql_name='paginationSimilarDocuments', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
))
    )
    is_read = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isRead')
    list_fact = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Fact'))), graphql_name='listFact')


class DocumentFeed(sgqlc.types.Type, RecordInterface):
    __schema__ = api_schema_new
    __field_names__ = ('id', 'name', 'search_string', 'pagination_document')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    search_string = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='searchString')
    pagination_document = sgqlc.types.Field(sgqlc.types.non_null(DocumentFromDocumentFeedPagination), graphql_name='paginationDocument', args=sgqlc.types.ArgDict((
        ('mode', sgqlc.types.Arg(DocumentFeedMode, graphql_name='mode', default='all')),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
        ('filter_settings', sgqlc.types.Arg(DocumentFilterSettings, graphql_name='filterSettings', default=None)),
        ('direction', sgqlc.types.Arg(SortDirection, graphql_name='direction', default='descending')),
        ('sort_field', sgqlc.types.Arg(DocumentSorting, graphql_name='sortField', default=None)),
        ('extra_settings', sgqlc.types.Arg(sgqlc.types.non_null(ExtraSettings), graphql_name='extraSettings', default=None)),
))
    )


class ExportTask(sgqlc.types.Type, RecordInterface):
    __schema__ = api_schema_new
    __field_names__ = ('id', 'entities', 'params', 'state', 'active', 'result', 'create_time', 'exporter')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    entities = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ExportEntity))), graphql_name='entities')
    params = sgqlc.types.Field(sgqlc.types.non_null(JSON), graphql_name='params')
    state = sgqlc.types.Field(sgqlc.types.non_null(ExportTaskState), graphql_name='state')
    active = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='active')
    result = sgqlc.types.Field(ExportResults, graphql_name='result')
    create_time = sgqlc.types.Field(sgqlc.types.non_null(UnixTime), graphql_name='createTime')
    exporter = sgqlc.types.Field('Exporter', graphql_name='exporter')


class Exporter(sgqlc.types.Type, RecordInterface):
    __schema__ = api_schema_new
    __field_names__ = ('id', 'title', 'menu_title', 'description', 'params_schema', 'default_params_schema', 'default_params', 'concept_type_ids', 'can_export_document', 'can_export_concept', 'can_export_one_entity', 'can_export_multiple_entities', 'last_task_time', 'metrics')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    menu_title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='menuTitle')
    description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='description')
    params_schema = sgqlc.types.Field(sgqlc.types.non_null(ParamsSchema), graphql_name='paramsSchema')
    default_params_schema = sgqlc.types.Field(sgqlc.types.non_null(ParamsSchema), graphql_name='defaultParamsSchema')
    default_params = sgqlc.types.Field(sgqlc.types.non_null(JSON), graphql_name='defaultParams')
    concept_type_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='conceptTypeIds')
    can_export_document = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='canExportDocument')
    can_export_concept = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='canExportConcept')
    can_export_one_entity = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='canExportOneEntity')
    can_export_multiple_entities = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='canExportMultipleEntities')
    last_task_time = sgqlc.types.Field(UnixTime, graphql_name='lastTaskTime')
    metrics = sgqlc.types.Field(sgqlc.types.non_null(KafkaTopicMetrics), graphql_name='metrics')


class InformationSourceLoader(sgqlc.types.Type, RecordInterface):
    __schema__ = api_schema_new
    __field_names__ = ('id', 'file', 'sources', 'title', 'is_retrospective', 'retrospective_start', 'retrospective_end', 'actual_status', 'status', 'metrics')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    file = sgqlc.types.Field(FileData, graphql_name='file')
    sources = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(InformationSourceData))), graphql_name='sources')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    is_retrospective = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isRetrospective')
    retrospective_start = sgqlc.types.Field(UnixTime, graphql_name='retrospectiveStart')
    retrospective_end = sgqlc.types.Field(UnixTime, graphql_name='retrospectiveEnd')
    actual_status = sgqlc.types.Field(sgqlc.types.non_null(InformationSourceLoaderActualStatus), graphql_name='actualStatus')
    status = sgqlc.types.Field(sgqlc.types.non_null(CollectionStatus), graphql_name='status')
    metrics = sgqlc.types.Field(sgqlc.types.non_null(InformationSourceLoaderStats), graphql_name='metrics')


class Issue(sgqlc.types.Type, RecordInterface):
    __schema__ = api_schema_new
    __field_names__ = ('id', 'topic', 'description', 'status', 'priority', 'execution_time_limit', 'markers', 'executor', 'pagination_document', 'pagination_concept', 'pagination_issue', 'metric', 'pagination_issue_change')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    topic = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='topic')
    description = sgqlc.types.Field(String, graphql_name='description')
    status = sgqlc.types.Field(sgqlc.types.non_null(IssueStatus), graphql_name='status')
    priority = sgqlc.types.Field(sgqlc.types.non_null(IssuePriority), graphql_name='priority')
    execution_time_limit = sgqlc.types.Field(UnixTime, graphql_name='executionTimeLimit')
    markers = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='markers')
    executor = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='executor')
    pagination_document = sgqlc.types.Field(sgqlc.types.non_null(DocumentPagination), graphql_name='paginationDocument', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
))
    )
    pagination_concept = sgqlc.types.Field(sgqlc.types.non_null(ConceptPagination), graphql_name='paginationConcept', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
))
    )
    pagination_issue = sgqlc.types.Field(sgqlc.types.non_null(IssuePagination), graphql_name='paginationIssue', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(IssueFilterSettings), graphql_name='filterSettings', default=None)),
        ('sort_direction', sgqlc.types.Arg(sgqlc.types.non_null(SortDirection), graphql_name='sortDirection', default=None)),
        ('sorting', sgqlc.types.Arg(sgqlc.types.non_null(IssueSorting), graphql_name='sorting', default=None)),
))
    )
    metric = sgqlc.types.Field(sgqlc.types.non_null(IssueStatistics), graphql_name='metric')
    pagination_issue_change = sgqlc.types.Field(sgqlc.types.non_null(IssueChangePagination), graphql_name='paginationIssueChange', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
))
    )


class IssueChange(sgqlc.types.Type, RecordInterface):
    __schema__ = api_schema_new
    __field_names__ = ('id', 'from_', 'to', 'comment')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    from_ = sgqlc.types.Field(sgqlc.types.non_null(IssueInfo), graphql_name='from')
    to = sgqlc.types.Field(sgqlc.types.non_null(IssueInfo), graphql_name='to')
    comment = sgqlc.types.Field(String, graphql_name='comment')


class Job(sgqlc.types.Type, RecordInterface):
    __schema__ = api_schema_new
    __field_names__ = ('id', 'status', 'priority', 'start_time', 'end_time', 'collection_status', 'is_noise', 'crawler', 'project', 'version', 'periodic', 'settings', 'args', 'metrics', 'job_stats', 'histogram_requests', 'histogram_items', 'schema')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    status = sgqlc.types.Field(sgqlc.types.non_null(JobStatus), graphql_name='status')
    priority = sgqlc.types.Field(sgqlc.types.non_null(JobPriorityType), graphql_name='priority')
    start_time = sgqlc.types.Field(Long, graphql_name='startTime')
    end_time = sgqlc.types.Field(Long, graphql_name='endTime')
    collection_status = sgqlc.types.Field(sgqlc.types.non_null(CollectionStatus), graphql_name='collectionStatus')
    is_noise = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isNoise')
    crawler = sgqlc.types.Field(sgqlc.types.non_null(CrawlerData), graphql_name='crawler')
    project = sgqlc.types.Field(sgqlc.types.non_null(ProjectData), graphql_name='project')
    version = sgqlc.types.Field(sgqlc.types.non_null(VersionData), graphql_name='version')
    periodic = sgqlc.types.Field(PeriodicJobData, graphql_name='periodic')
    settings = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(KeyValue))), graphql_name='settings')
    args = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(KeyValue))), graphql_name='args')
    metrics = sgqlc.types.Field(sgqlc.types.non_null(JobMetrics), graphql_name='metrics')
    job_stats = sgqlc.types.Field(JobStats, graphql_name='jobStats')
    histogram_requests = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(DateHistogramBucket))), graphql_name='histogramRequests')
    histogram_items = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(DateHistogramBucket))), graphql_name='histogramItems')
    schema = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(KeyValue))), graphql_name='schema')


class KafkaTopic(sgqlc.types.Type, RecordInterface):
    __schema__ = api_schema_new
    __field_names__ = ('topic', 'description', 'pipeline', 'metrics', 'priority', 'request_timeout_ms', 'move_to_on_timeout', 'system_topic')
    topic = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='topic')
    description = sgqlc.types.Field(String, graphql_name='description')
    pipeline = sgqlc.types.Field(PipelineSetup, graphql_name='pipeline')
    metrics = sgqlc.types.Field(sgqlc.types.non_null(KafkaTopicMetrics), graphql_name='metrics')
    priority = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='priority')
    request_timeout_ms = sgqlc.types.Field(Int, graphql_name='requestTimeoutMs')
    move_to_on_timeout = sgqlc.types.Field(String, graphql_name='moveToOnTimeout')
    system_topic = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='systemTopic')


class PeriodicJob(sgqlc.types.Type, RecordInterface):
    __schema__ = api_schema_new
    __field_names__ = ('id', 'name', 'description', 'project', 'crawler', 'version', 'priority', 'status', 'cron', 'cron_utcoffset_minutes', 'next_schedule_time', 'update_on_reload', 'settings', 'args', 'metrics', 'histogram_requests', 'histogram_items', 'job_stats')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    description = sgqlc.types.Field(String, graphql_name='description')
    project = sgqlc.types.Field(sgqlc.types.non_null(ProjectData), graphql_name='project')
    crawler = sgqlc.types.Field(sgqlc.types.non_null(CrawlerData), graphql_name='crawler')
    version = sgqlc.types.Field(sgqlc.types.non_null(VersionData), graphql_name='version')
    priority = sgqlc.types.Field(sgqlc.types.non_null(JobPriorityType), graphql_name='priority')
    status = sgqlc.types.Field(sgqlc.types.non_null(PeriodicJobStatus), graphql_name='status')
    cron = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cron')
    cron_utcoffset_minutes = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='cronUTCOffsetMinutes')
    next_schedule_time = sgqlc.types.Field(Long, graphql_name='nextScheduleTime')
    update_on_reload = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateOnReload')
    settings = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(KeyValue))), graphql_name='settings')
    args = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(KeyValue))), graphql_name='args')
    metrics = sgqlc.types.Field(sgqlc.types.non_null(PeriodicJobMetrics), graphql_name='metrics')
    histogram_requests = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(DateHistogramBucket))), graphql_name='histogramRequests', args=sgqlc.types.ArgDict((
        ('interval', sgqlc.types.Arg(TimestampInterval, graphql_name='interval', default=None)),
))
    )
    histogram_items = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(DateHistogramBucket))), graphql_name='histogramItems', args=sgqlc.types.ArgDict((
        ('interval', sgqlc.types.Arg(TimestampInterval, graphql_name='interval', default=None)),
))
    )
    job_stats = sgqlc.types.Field(sgqlc.types.non_null(JobStats), graphql_name='jobStats', args=sgqlc.types.ArgDict((
        ('interval', sgqlc.types.Arg(TimestampInterval, graphql_name='interval', default=None)),
))
    )


class PeriodicTask(sgqlc.types.Type, RecordInterface):
    __schema__ = api_schema_new
    __field_names__ = ('id', 'task_type', 'title', 'description', 'status', 'access_level', 'trust_level', 'topic', 'next_schedule_time', 'cron', 'cron_utcoffset_minutes', 'metrics', 'import_metrics', 'config')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    task_type = sgqlc.types.Field(sgqlc.types.non_null(TaskType), graphql_name='taskType')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    description = sgqlc.types.Field(String, graphql_name='description')
    status = sgqlc.types.Field(sgqlc.types.non_null(RunningStatus), graphql_name='status')
    access_level = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='accessLevel')
    trust_level = sgqlc.types.Field(sgqlc.types.non_null(TrustLevel), graphql_name='trustLevel')
    topic = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='topic')
    next_schedule_time = sgqlc.types.Field(Instant, graphql_name='nextScheduleTime')
    cron = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cron')
    cron_utcoffset_minutes = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='cronUTCOffsetMinutes')
    metrics = sgqlc.types.Field(sgqlc.types.non_null(PeriodicTaskMetrics), graphql_name='metrics')
    import_metrics = sgqlc.types.Field(sgqlc.types.non_null(PeriodicTaskImportMetrics), graphql_name='importMetrics')
    config = sgqlc.types.Field(sgqlc.types.non_null('TaskConfig'), graphql_name='config')


class PipelineConfig(sgqlc.types.Type, RecordInterface):
    __schema__ = api_schema_new
    __field_names__ = ('id', 'description', 'transforms', 'transform_count', 'used_in_topics')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='description')
    transforms = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(PipelineTransformSetup))), graphql_name='transforms')
    transform_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='transformCount')
    used_in_topics = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='usedInTopics')


class Platform(sgqlc.types.Type, RecordInterface):
    __schema__ = api_schema_new
    __field_names__ = ('id', 'name', 'platform_type', 'url', 'country', 'language', 'markers', 'params', 'image', 'metric', 'period', 'accounts')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    platform_type = sgqlc.types.Field(sgqlc.types.non_null(PlatformType), graphql_name='platformType')
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')
    country = sgqlc.types.Field(String, graphql_name='country')
    language = sgqlc.types.Field(String, graphql_name='language')
    markers = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='markers')
    params = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Parameter))), graphql_name='params')
    image = sgqlc.types.Field(Image, graphql_name='image')
    metric = sgqlc.types.Field(sgqlc.types.non_null(PlatformStatistics), graphql_name='metric')
    period = sgqlc.types.Field(sgqlc.types.non_null(DateTimeInterval), graphql_name='period')
    accounts = sgqlc.types.Field(sgqlc.types.non_null(AccountPagination), graphql_name='accounts', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(AccountFilterSettings), graphql_name='filterSettings', default=None)),
        ('sort_direction', sgqlc.types.Arg(SortDirection, graphql_name='sortDirection', default='descending')),
        ('sorting', sgqlc.types.Arg(AccountSorting, graphql_name='sorting', default='id')),
))
    )


class Project(sgqlc.types.Type, RecordInterface):
    __schema__ = api_schema_new
    __field_names__ = ('id', 'name', 'title', 'description', 'crawlers_num', 'periodic_jobs_num', 'jobs_num', 'active', 'settings', 'args', 'project_stats', 'histogram_items', 'histogram_crawlers', 'current_version', 'egg_file')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    description = sgqlc.types.Field(String, graphql_name='description')
    crawlers_num = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='crawlersNum')
    periodic_jobs_num = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='periodicJobsNum')
    jobs_num = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='jobsNum')
    active = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='active')
    settings = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(KeyValue))), graphql_name='settings')
    args = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(KeyValue))), graphql_name='args')
    project_stats = sgqlc.types.Field(sgqlc.types.non_null(ProjectStats), graphql_name='projectStats', args=sgqlc.types.ArgDict((
        ('interval', sgqlc.types.Arg(TimestampInterval, graphql_name='interval', default=None)),
))
    )
    histogram_items = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(DateHistogramBucket))), graphql_name='histogramItems', args=sgqlc.types.ArgDict((
        ('interval', sgqlc.types.Arg(TimestampInterval, graphql_name='interval', default=None)),
))
    )
    histogram_crawlers = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CrawlerHistogram))), graphql_name='histogramCrawlers', args=sgqlc.types.ArgDict((
        ('interval', sgqlc.types.Arg(TimestampInterval, graphql_name='interval', default=None)),
))
    )
    current_version = sgqlc.types.Field('Version', graphql_name='currentVersion')
    egg_file = sgqlc.types.Field(String, graphql_name='eggFile')


class RecordInterfaceCommonFields(sgqlc.types.Type, RecordInterface):
    __schema__ = api_schema_new
    __field_names__ = ()


class ResearchMap(sgqlc.types.Type, RecordInterface):
    __schema__ = api_schema_new
    __field_names__ = ('id', 'name', 'description', 'is_temporary', 'markers', 'list_node', 'list_edge', 'research_map_statistics', 'list_group', 'is_active', 'access_level', 'pagination_concept', 'pagination_story', 'pagination_research_map')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    description = sgqlc.types.Field(String, graphql_name='description')
    is_temporary = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isTemporary')
    markers = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='markers')
    list_node = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(MapNode))), graphql_name='listNode', args=sgqlc.types.ArgDict((
        ('filter_settings', sgqlc.types.Arg(MapNodeFilterSettings, graphql_name='filterSettings', default=None)),
        ('default_view', sgqlc.types.Arg(Boolean, graphql_name='defaultView', default=True)),
))
    )
    list_edge = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(MapEdge))), graphql_name='listEdge', args=sgqlc.types.ArgDict((
        ('filter_settings', sgqlc.types.Arg(MapEdgeFilterSettings, graphql_name='filterSettings', default=None)),
        ('default_view', sgqlc.types.Arg(Boolean, graphql_name='defaultView', default=True)),
))
    )
    research_map_statistics = sgqlc.types.Field(sgqlc.types.non_null(ResearchMapStatistics), graphql_name='researchMapStatistics')
    list_group = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Group))), graphql_name='listGroup')
    is_active = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isActive')
    access_level = sgqlc.types.Field(sgqlc.types.non_null(AccessLevel), graphql_name='accessLevel')
    pagination_concept = sgqlc.types.Field(sgqlc.types.non_null(ConceptPagination), graphql_name='paginationConcept', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
        ('filter_settings', sgqlc.types.Arg(ConceptFilterSettings, graphql_name='filterSettings', default=None)),
        ('direction', sgqlc.types.Arg(SortDirection, graphql_name='direction', default='descending')),
        ('sort_field', sgqlc.types.Arg(ConceptSorting, graphql_name='sortField', default=None)),
        ('extra_settings', sgqlc.types.Arg(sgqlc.types.non_null(ConceptExtraSettings), graphql_name='extraSettings', default=None)),
))
    )
    pagination_story = sgqlc.types.Field(sgqlc.types.non_null(StoryPagination), graphql_name='paginationStory', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('grouping', sgqlc.types.Arg(DocumentGrouping, graphql_name='grouping', default='none')),
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
        ('filter_settings', sgqlc.types.Arg(DocumentFilterSettings, graphql_name='filterSettings', default=None)),
        ('direction', sgqlc.types.Arg(SortDirection, graphql_name='direction', default='descending')),
        ('sort_field', sgqlc.types.Arg(DocumentSorting, graphql_name='sortField', default=None)),
        ('extra_settings', sgqlc.types.Arg(sgqlc.types.non_null(ExtraSettings), graphql_name='extraSettings', default=None)),
))
    )
    pagination_research_map = sgqlc.types.Field(sgqlc.types.non_null(ResearchMapPagination), graphql_name='paginationResearchMap', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(ResearchMapFilterSettings), graphql_name='filterSettings', default=None)),
        ('direction', sgqlc.types.Arg(SortDirection, graphql_name='direction', default='descending')),
        ('sort_field', sgqlc.types.Arg(ResearchMapSorting, graphql_name='sortField', default='conceptAndDocumentLink')),
        ('research_map_content_select_input', sgqlc.types.Arg(ResearchMapContentUpdateInput, graphql_name='ResearchMapContentSelectInput', default=None)),
))
    )


class SearchObject(sgqlc.types.Type, RecordInterface):
    __schema__ = api_schema_new
    __field_names__ = ('id', 'name', 'target', 'search_container', 'missing_concept_property_types')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    target = sgqlc.types.Field(sgqlc.types.non_null(SearchTarget), graphql_name='target')
    search_container = sgqlc.types.Field(sgqlc.types.non_null('SearchContainer'), graphql_name='searchContainer')
    missing_concept_property_types = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ConceptPropertyType))), graphql_name='missingConceptPropertyTypes')


class Task(sgqlc.types.Type, RecordInterface):
    __schema__ = api_schema_new
    __field_names__ = ('id', 'task_type', 'periodic_task', 'access_level', 'trust_level', 'topic', 'task_status', 'start_time', 'end_time', 'collection_status', 'metrics', 'import_metrics', 'config')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    task_type = sgqlc.types.Field(sgqlc.types.non_null(TaskType), graphql_name='taskType')
    periodic_task = sgqlc.types.Field(PeriodicTask, graphql_name='periodicTask')
    access_level = sgqlc.types.Field(ID, graphql_name='accessLevel')
    trust_level = sgqlc.types.Field(TrustLevel, graphql_name='trustLevel')
    topic = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='topic')
    task_status = sgqlc.types.Field(sgqlc.types.non_null(TaskStatus), graphql_name='taskStatus')
    start_time = sgqlc.types.Field(UnixTime, graphql_name='startTime')
    end_time = sgqlc.types.Field(UnixTime, graphql_name='endTime')
    collection_status = sgqlc.types.Field(sgqlc.types.non_null(CollectionStatus), graphql_name='collectionStatus')
    metrics = sgqlc.types.Field(sgqlc.types.non_null(TaskMetrics), graphql_name='metrics')
    import_metrics = sgqlc.types.Field(sgqlc.types.non_null(TaskImportMetrics), graphql_name='importMetrics')
    config = sgqlc.types.Field(sgqlc.types.non_null('TaskConfig'), graphql_name='config')


class User(sgqlc.types.Type, RecordInterface):
    __schema__ = api_schema_new
    __field_names__ = ('id', 'login', 'first_name', 'last_name', 'fathers_name', 'email', 'is_admin', 'enabled', 'receive_notifications', 'access_level', 'name', 'list_user_group', 'metrics', 'attributes', 'allowed_functions')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    login = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='login')
    first_name = sgqlc.types.Field(String, graphql_name='firstName')
    last_name = sgqlc.types.Field(String, graphql_name='lastName')
    fathers_name = sgqlc.types.Field(String, graphql_name='fathersName')
    email = sgqlc.types.Field(String, graphql_name='email')
    is_admin = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isAdmin')
    enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='enabled')
    receive_notifications = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='receiveNotifications')
    access_level = sgqlc.types.Field(sgqlc.types.non_null(AccessLevel), graphql_name='accessLevel')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    list_user_group = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserGroup'))), graphql_name='listUserGroup')
    metrics = sgqlc.types.Field(sgqlc.types.non_null(UserMetrics), graphql_name='metrics')
    attributes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(UserAttribute))), graphql_name='attributes', args=sgqlc.types.ArgDict((
        ('show_default', sgqlc.types.Arg(Boolean, graphql_name='showDefault', default=False)),
        ('is_request_from_front', sgqlc.types.Arg(Boolean, graphql_name='isRequestFromFront', default=True)),
))
    )
    allowed_functions = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AllowedFunctionsEnum))), graphql_name='allowedFunctions')


class UserGroup(sgqlc.types.Type, RecordInterface):
    __schema__ = api_schema_new
    __field_names__ = ('id', 'name', 'description', 'attributes', 'list_user', 'metrics')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    description = sgqlc.types.Field(String, graphql_name='description')
    attributes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(UserAttribute))), graphql_name='attributes')
    list_user = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(User))), graphql_name='listUser')
    metrics = sgqlc.types.Field(sgqlc.types.non_null(UserGroupMetrics), graphql_name='metrics')


class UserPipelineTransform(sgqlc.types.Type, RecordInterface):
    __schema__ = api_schema_new
    __field_names__ = ('id', 'description', 'in_type', 'out_type', 'used_in_pipeline_configs', 'version', 'service')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    description = sgqlc.types.Field(String, graphql_name='description')
    in_type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='inType')
    out_type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='outType')
    used_in_pipeline_configs = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='usedInPipelineConfigs')
    version = sgqlc.types.Field(String, graphql_name='version')
    service = sgqlc.types.Field(sgqlc.types.non_null(UserService), graphql_name='service')


class Version(sgqlc.types.Type, RecordInterface):
    __schema__ = api_schema_new
    __field_names__ = ('id', 'version_name', 'project_id', 'status')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    version_name = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='versionName')
    project_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='projectId')
    status = sgqlc.types.Field(sgqlc.types.non_null(VersionStatus), graphql_name='status')



########################################################################
# Unions
########################################################################
class AnyValue(sgqlc.types.Union):
    __schema__ = api_schema_new
    __types__ = (DateTimeValue, GeoPointValue, IntValue, DoubleValue, StringLocaleValue, StringValue, LinkValue, CompositeValue)


class AnyValueType(sgqlc.types.Union):
    __schema__ = api_schema_new
    __types__ = (ConceptPropertyValueType, CompositePropertyValueTemplate)


class ChartRData(sgqlc.types.Union):
    __schema__ = api_schema_new
    __types__ = (ChartAtomData, ChartAtomDataList, ChartSeriesDataList)


class ConceptLikeFact(sgqlc.types.Union):
    __schema__ = api_schema_new
    __types__ = (ConceptCandidateFact, ConceptFact)


class ConceptPropertyLikeFact(sgqlc.types.Union):
    __schema__ = api_schema_new
    __types__ = (ConceptPropertyFact, ConceptLinkPropertyFact)


class ConceptViewValue(sgqlc.types.Union):
    __schema__ = api_schema_new
    __types__ = (DateTimeValue, GeoPointValue, IntValue, DoubleValue, StringLocaleValue, StringValue, LinkValue, CompositeValue, Concept, ConceptType, ConceptLinkType, User)


class DashboardPanelData(sgqlc.types.Union):
    __schema__ = api_schema_new
    __types__ = (EmptyPanel, TaskPanel, ConceptPanel, DocumentPanel, ConceptViewPanel, ChartPanel)


class Entity(sgqlc.types.Union):
    __schema__ = api_schema_new
    __types__ = (Concept, Document, ConceptCandidateFact, ConceptType)


class EntityLink(sgqlc.types.Union):
    __schema__ = api_schema_new
    __types__ = (ConceptLink, ConceptFactLink, ConceptImplicitLink, ConceptCandidateFactMention, ConceptMention, DocumentLink, ConceptLinkCandidateFact, ConceptLinkType)


class ExternalSearch(sgqlc.types.Union):
    __schema__ = api_schema_new
    __types__ = (ExternalSearchJob, ExternalSearchTask)


class Fact(sgqlc.types.Union):
    __schema__ = api_schema_new
    __types__ = (ConceptCandidateFact, ConceptFact, ConceptLinkCandidateFact, ConceptLinkFact, ConceptPropertyCandidateFact, ConceptPropertyFact, ConceptPropertyValueCandidateFact, ConceptLinkPropertyFact)


class MessageStatusInfo(sgqlc.types.Union):
    __schema__ = api_schema_new
    __types__ = (MessageOk, MessageFailed, MessageDuplicate, MessageInProgress, MessageNotHandled, MessageUnknown)


class PendingMessageStatusInfo(sgqlc.types.Union):
    __schema__ = api_schema_new
    __types__ = (MessageInProgress, MessageNotHandled)


class SearchContainer(sgqlc.types.Union):
    __schema__ = api_schema_new
    __types__ = (ExternalSearchImportConfig, ExternalSearchJobConfig, FilterSettings, SearchQuery)


class TaskConfig(sgqlc.types.Union):
    __schema__ = api_schema_new
    __types__ = (DBConfig, FileRepositoryConfig, HTMLConfig, LocalConfig, ReportConfig)


class TypeSearchElement(sgqlc.types.Union):
    __schema__ = api_schema_new
    __types__ = (DictValue, NERCRegexp)


class UserMenuType(sgqlc.types.Union):
    __schema__ = api_schema_new
    __types__ = (ConceptType, CompositeConceptType, ConceptTypeView)


class Value(sgqlc.types.Union):
    __schema__ = api_schema_new
    __types__ = (DateTimeValue, GeoPointValue, IntValue, DoubleValue, StringLocaleValue, StringValue, LinkValue)



########################################################################
# Schema Entry Points
########################################################################
api_schema_new.query_type = Query
api_schema_new.mutation_type = Mutation
api_schema_new.subscription_type = Subscription

